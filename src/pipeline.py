"""Single reproducible entry point for the feedback's computational evidence requests."""
import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import numpy as np
from . import analysis, figures, screening
from .data import ROOT, digest, ensure_data


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def run(data_dir, output_dir, download=False, import_data=None):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    figure_dir = output / 'figures'
    figure_dir.mkdir(exist_ok=True)
    inputs = ensure_data(data_dir, download=download, import_folder=import_data)
    x, structure = analysis.read_and_check_tables(data_dir)
    stats, corr, pairs = analysis.describe(x)
    topology = analysis.nominal_topology(data_dir)
    counts = screening.recount()
    dump(output / 'table_checks.json', structure)
    dump(output / 'eda_statistics.json', stats)
    dump(output / 'topology_audit.json', topology)
    dump(output / 'screening_summary.json', counts)
    corr.to_csv(output / 'correlations.csv', index_label='variable', lineterminator='\n')
    x.head(20).to_csv(output / 'selected_inputs_sample.csv', index_label='forecast_origin', lineterminator='\n')
    pairs.head(20).to_csv(output / 'forecast_pairs_sample.csv', index_label='forecast_origin', lineterminator='\n')
    x.to_csv(output / 'selected_inputs_full.csv.gz', index_label='forecast_origin', compression='gzip', lineterminator='\n')
    pairs.to_csv(output / 'forecast_pairs_full.csv.gz', index_label='forecast_origin', compression='gzip', lineterminator='\n')
    figures.supply_boundary(topology, figure_dir)
    figures.daily_profiles(x, figure_dir)
    figures.correlations(corr, figure_dir)
    figures.screening(counts, figure_dir)

    # Expected values are fixed historical report claims, independent of this refactor.
    expected = json.loads((ROOT / 'evidence/reported_values.json').read_text(encoding='utf-8'))
    matches = []
    for key in ['rows', 'forecast_pairs', 'days']:
        assert stats[key] == expected[key], (key, stats[key], expected[key])
        matches.append(key)
    for key in ['persistence_MAE_m', 'persistence_RMSE_m']:
        assert abs(stats[key]-expected[key]) < 1e-12, (key, stats[key], expected[key])
        matches.append(key)
    assert np.allclose(stats['n1_range_m'], expected['n1_range_m'], atol=1e-12)
    for name, value in expected['correlation_with_future_n1'].items():
        assert abs(stats['correlation_with_future_n1'][name]-value) < 1e-10
    for name, distance in expected['T1_pipe_distances_m'].items():
        actual = topology['T1_to_measured_pressure_nodes'][name]['distance_m']
        assert round(actual) == distance, (name, actual, distance)
        assert abs(actual-expected['T1_pipe_distances_unrounded_m'][name]) < 1e-8
    assert counts['source_records'] == 47 and counts['groups'] == 35
    assert [r['groups'] for r in counts['categories']] == [27, 3, 2, 2, 1]
    assert topology['network_counts'] == expected['network_counts']
    assert topology['sectors']['C']['junctions'] == 92
    assert topology['sectors']['C']['pressure_sensors'] == ['n1', 'n4', 'n31']
    assert topology['sectors']['C']['AMR_count'] == 82
    checks = {'expected_numeric_claims_match': True, 'table_checks_pass': True,
              'reported_2018_correlations_match': True, 'reported_pipe_distances_match': True,
              'historical_inventory_counts_match': True, 'models_trained': False,
              '2019_use': 'Annual table-structure checks; forecasting assessment belongs to the proposed modeling stage.',
              'figure_reproduction': 'Same source quantities and plotting procedure, with portable fonts and separately preserved submitted images.',
              'research_attribution': 'Student-directed research with AI-assisted methodological development, code generation and execution; see docs/student_contributions.md.'}
    dump(output / 'verification.json', checks)
    output_hashes = {str(path.relative_to(output)).replace('\\', '/'): digest(path)
                     for path in sorted(output.rglob('*')) if path.is_file() and (path.parent == figure_dir or path.name in ['table_checks.json', 'eda_statistics.json', 'topology_audit.json', 'screening_summary.json', 'correlations.csv', 'selected_inputs_sample.csv', 'forecast_pairs_sample.csv', 'selected_inputs_full.csv.gz', 'forecast_pairs_full.csv.gz', 'verification.json'])}
    code_hashes = {str(path.relative_to(ROOT)).replace('\\', '/'): digest(path)
                   for path in sorted((ROOT / 'src').glob('*.py'))}
    code_hashes['reproduce.py'] = digest(ROOT / 'reproduce.py')
    classification_inputs = {name: digest(ROOT / name) for name in [
        'literature/source_records.csv', 'literature/groups.csv',
        'data/source_manifest.json', 'evidence/reported_values.json',
        'evidence/contribution_summary.csv', 'evidence/work_status.json', 'docs/student_contributions.md']}
    manifest = {
        'run_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version, 'platform': platform.platform(),
        'packages': {n: importlib.metadata.version(n) for n in ['numpy', 'pandas', 'matplotlib', 'PyYAML']},
        'inputs': inputs, 'code_sha256': code_hashes, 'classification_and_protocol_sha256': classification_inputs,
        'output_sha256': output_hashes,
        'results_status': 'Executed descriptive groundwork; C1–C3 learning experiments remain proposed.',
        'authorship': 'Andres Arango Martinez directed the engineering focus, scope, choices and review. AI assisted methodological proposals, source synthesis, implementation and execution; external data/methods retain their attribution.',
    }
    dump(output / 'run_manifest.json', manifest)
    print(json.dumps({'status': 'PASS', 'rows': stats['rows'], 'pairs': stats['forecast_pairs'],
                      'MAE_m': stats['persistence_MAE_m'], 'RMSE_m': stats['persistence_RMSE_m'],
                      'groups': counts['groups'], 'models_trained': False}, indent=2), flush=True)
    return stats, topology, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=ROOT / 'data/raw')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'results')
    parser.add_argument('--download', action='store_true', help='Download missing official files and verify their published MD5.')
    parser.add_argument('--import-data', type=Path, help='Optional flat cache of the exact official files; every checksum is checked.')
    args = parser.parse_args()
    run(args.data_dir, args.output_dir, args.download, args.import_data)
