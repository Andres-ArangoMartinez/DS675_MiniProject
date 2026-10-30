"""Checks, past/future alignment, descriptive EDA and nominal pipe-graph distances."""
from collections import defaultdict
from pathlib import Path
import heapq
import numpy as np
import pandas as pd
import yaml

SIGNALS = ['n1', 'n4', 'n31', 'T1', 'PUMP_1', 'AMR_n1']
TARGET = 'n1_plus15'
PERIOD_START = '2018-01-01'
PERIOD_END = '2018-09-30'


def read_and_check_tables(raw):
    """2019 is read for structural checks only; no 2019 prediction score is computed."""
    raw = Path(raw)
    structural = []
    training = {}
    for year in [2018, 2019]:
        previous_index = None
        for kind, columns in [('Pressures', 33), ('Flows', 3), ('Levels', 1), ('Demands', 82)]:
            name = f'{year}_SCADA_{kind}.csv'
            frame = pd.read_csv(raw / name, sep=';', decimal=',', index_col=0, parse_dates=True)
            if frame.shape != (105120, columns):
                raise ValueError(f'Unexpected shape: {name}: {frame.shape}')
            assert frame.index.is_unique and frame.index.is_monotonic_increasing
            assert frame.index.to_series().diff().dropna().eq(pd.Timedelta(minutes=5)).all()
            assert not frame.isna().any().any()
            assert frame.index[0] == pd.Timestamp(f'{year}-01-01 00:00')
            assert frame.index[-1] == pd.Timestamp(f'{year}-12-31 23:55')
            if previous_index is not None:
                assert frame.index.equals(previous_index), f'Timestamp mismatch: {name}'
            previous_index = frame.index
            structural.append({
                'filename': name, 'year': year, 'records': len(frame), 'features': columns,
                'duplicate_timestamps': 0, 'missing_values': 0, 'spacing_minutes': 5,
                'timestamps_match_other_tables_in_year': True,
                'use': 'structure_and_Jan_Sep_EDA' if year == 2018 else 'structure_only',
            })
            if year == 2018:
                training[kind] = frame.loc[PERIOD_START:PERIOD_END].copy()
            print(f'Checked {name}: {len(frame):,} rows, {columns} channels', flush=True)
    pressures = training['Pressures']
    x = pressures[['n1', 'n4', 'n31']].join(training['Levels'][['T1']])
    x = x.join(training['Flows'][['PUMP_1']])
    x = x.join(training['Demands'][['n1']].rename(columns={'n1': 'AMR_n1'}))
    assert list(x.columns) == SIGNALS and x.shape == (78624, 6)
    return x, structural


def make_forecast_pairs(x, steps=3):
    """Crop the period first, then shift: the final 3 labels cannot cross September."""
    if steps < 1:
        raise ValueError('The forecast lead must be positive.')
    if not x.index.is_unique or not x.index.is_monotonic_increasing:
        raise ValueError('Forecast origins must be unique and ordered.')
    if not x.index.to_series().diff().dropna().eq(pd.Timedelta(minutes=5)).all():
        raise ValueError('Row shifts require uninterrupted five-minute spacing.')
    pairs = x.copy()
    pairs[TARGET] = x['n1'].shift(-steps)
    pairs = pairs.dropna()
    return pairs


def describe(x):
    pairs = make_forecast_pairs(x)
    error = pairs[TARGET] - pairs['n1']
    corr = pairs.corr(method='pearson')
    statistics = {
        'period_start': PERIOD_START, 'period_end': PERIOD_END, 'days': int(x.index.normalize().nunique()),
        'rows': len(x), 'forecast_pairs': len(pairs), 'lead_minutes': 15,
        'n1_range_m': [float(x.n1.min()), float(x.n1.max())],
        'persistence_MAE_m': float(error.abs().mean()),
        'persistence_RMSE_m': float(np.sqrt((error ** 2).mean())),
        'correlation_with_future_n1': {name: float(corr.loc[name, TARGET]) for name in SIGNALS},
        'signals': SIGNALS, 'target': TARGET,
        'interpretation': 'Descriptive Jan-Sep 2018 results; not a final 2019 test score.',
        'learned_models_fitted': False,
    }
    assert len(pairs) == 78621
    return statistics, corr, pairs


def parse_inp(path):
    sections = {}
    section = None
    for line in Path(path).read_text(encoding='utf-8-sig').splitlines():
        text = line.split(';', 1)[0].strip()
        if text.startswith('['):
            section = text.upper()
            sections[section] = []
        elif text and section:
            sections[section].append(text.split())
    return sections


def nominal_topology(raw):
    """Undirected, initially open pipe graph; excludes pumps and PRVs as boundaries."""
    raw = Path(raw)
    sections = parse_inp(raw / 'L-TOWN.inp')
    config = yaml.safe_load((raw / 'dataset_configuration.yaml').read_text(encoding='utf-8'))
    graph = defaultdict(list)
    closed = []
    for row in sections['[PIPES]']:
        if len(row) > 7 and row[7].upper() == 'CLOSED':
            closed.append(row[0])
            continue
        left, right, length = row[1], row[2], float(row[3])
        graph[left].append((right, length, row[0]))
        graph[right].append((left, length, row[0]))

    def component(root):
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(peer for peer, _, _ in graph[node] if peer not in seen)
        return seen

    distances = {}
    paths = {}
    queue = [(0.0, 'T1', ())]
    while queue:
        distance, node, pipes = heapq.heappop(queue)
        if node in distances:
            continue
        distances[node] = distance
        paths[node] = list(pipes)
        for peer, length, pipe in graph[node]:
            if peer not in distances:
                heapq.heappush(queue, (distance + length, peer, pipes + (pipe,)))

    junctions = {row[0] for row in sections['[JUNCTIONS]']}
    sectors = {}
    components = {}
    for area, root in [('A', 'n300'), ('B', 'n226'), ('C', 'T1')]:
        nodes = component(root)
        components[area] = nodes
        sensors = [node for node in config['pressure_sensors'] if node in nodes]
        sectors[area] = {
            'junctions': len(nodes & junctions), 'pressure_sensors': sensors,
            'pressure_sensor_count': len(sensors), 'AMR_count': len(set(config['amrs']) & nodes),
        }
    assert not any(components[a] & components[b] for a, b in [('A', 'B'), ('A', 'C'), ('B', 'C')])
    upstream = sorted(junctions - set.union(*components.values()))
    assert sum(s['junctions'] for s in sectors.values()) + len(upstream) == 782
    measured_distances = {node: {'distance_m': distances[node], 'pipe_path': paths[node]} for node in ['n1', 'n4', 'n31']}
    boundary_pipes = [r for r in sections['[PIPES]'] if r[0] in ['p227', 'p235', 'p239']]
    assert {(r[0], r[1], r[2]) for r in boundary_pipes} == {('p227', 'R1', 'n303'), ('p235', 'R2', 'n336'), ('p239', 'T1', 'n343')}
    assert any(r[:3] == ['PUMP_1', 'n54', 'T1'] for r in sections['[PUMPS]'])
    return {
        'model': 'L-TOWN.inp (nominal)', 'algorithm': 'Dijkstra shortest total pipe length from T1',
        'scope': 'Initially open undirected pipes; pumps and PRVs excluded from sector connections.',
        'network_counts': {name: len(sections[key]) for name, key in [
            ('junctions', '[JUNCTIONS]'), ('reservoirs', '[RESERVOIRS]'), ('tanks', '[TANKS]'),
            ('pipes', '[PIPES]'), ('pumps', '[PUMPS]'), ('valves', '[VALVES]')]},
        'sectors': sectors, 'upstream_boundary_junctions': upstream, 'closed_pipes_excluded': closed,
        'T1_to_measured_pressure_nodes': measured_distances,
        'PRVs': [{'id': r[0], 'from': r[1], 'to': r[2], 'type': r[4], 'nominal_setting_m': float(r[5])} for r in sections['[VALVES]']],
        'supply_schematic_evidence': {
            'reservoirs': [r[0] for r in sections['[RESERVOIRS]']],
            'pumps': [{'id': r[0], 'from': r[1], 'to': r[2]} for r in sections['[PUMPS]']],
            'boundary_pipes': [{'id': r[0], 'from': r[1], 'to': r[2]} for r in boundary_pipes],
            'note': 'Connectivity verified in nominal model; figure layout and supply arrows are interpretive, not solved hydraulic flows.'},
        'nominal_controls': [' '.join(row) for row in sections['[CONTROLS]']],
        'feature_filter_counts': {'all_channels': len(config['pressure_sensors']) + len(config['flow_sensors']) + len(config['level_sensors']) + len(config['amrs']), 'Area_C_and_pump_candidates': sectors['C']['pressure_sensor_count'] + sectors['C']['AMR_count'] + 2, 'selected_signals': len(SIGNALS)},
        'limitations': [
            'Pipe-path length is not hydraulic sensitivity, pressure propagation delay or travel time.',
            'Nominal setpoints do not establish observed time-varying valve states.',
            'A tank supply boundary does not prove statistical independence from upstream conditions.',
            'PUMP_1 is tank inflow; AMR_n1 is nodal consumption, not sector inflow.',
        ],
    }
