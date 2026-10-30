"""Checks that protect the report's chronology, data identity and counting claims."""
import csv
import json
from pathlib import Path
import tempfile
import unittest
import numpy as np
import pandas as pd
from src.analysis import make_forecast_pairs, TARGET, nominal_topology
from src.data import ROOT, digest, source_manifest
from src.screening import recount


class EvidenceTests(unittest.TestCase):
    def test_exact_future_time_and_period_end(self):
        index = pd.date_range('2018-09-30 23:20', periods=8, freq='5min')
        x = pd.DataFrame({'n1': np.arange(8, dtype=float)}, index=index)
        pairs = make_forecast_pairs(x)
        self.assertEqual(len(pairs), 5)
        self.assertEqual(pairs.index[-1], pd.Timestamp('2018-09-30 23:40'))
        for origin, row in pairs.iterrows():
            self.assertEqual(row[TARGET], x.loc[origin + pd.Timedelta(minutes=15), 'n1'])
            self.assertEqual(row['n1'], x.loc[origin, 'n1'])
        self.assertLessEqual(pairs.index[-1] + pd.Timedelta(minutes=15), x.index[-1])

    def test_missing_time_cannot_silently_change_the_lead(self):
        idx = pd.date_range('2018-01-01', periods=9, freq='5min').delete(3)
        with self.assertRaises(ValueError):
            make_forecast_pairs(pd.DataFrame({'n1': range(8)}, index=idx))

    def test_duplicate_origin_rejected(self):
        idx = pd.to_datetime(['2018-01-01', '2018-01-01'])
        with self.assertRaises(ValueError):
            make_forecast_pairs(pd.DataFrame({'n1': [1, 2]}, index=idx))

    def test_every_official_input_checksum(self):
        for source in source_manifest()['files']:
            path = ROOT / 'data/raw' / source['filename']
            self.assertTrue(path.exists(), 'Run reproduce.py first to obtain official files.')
            self.assertEqual(path.stat().st_size, source['bytes'], source['filename'])
            self.assertEqual(digest(path, 'md5'), source['md5'], source['filename'])

    def test_independent_pressure_calculation(self):
        p = pd.read_csv(ROOT / 'data/raw/2018_SCADA_Pressures.csv', sep=';', decimal=',', index_col=0, parse_dates=True)
        values = p.loc['2018-01-01':'2018-09-30', 'n1'].to_numpy()
        error = values[3:] - values[:-3]
        self.assertEqual(len(values), 78624)
        self.assertEqual(len(error), 78621)
        self.assertAlmostEqual(np.abs(error).mean(), 0.05177624298851451, places=12)
        self.assertAlmostEqual(np.sqrt(np.mean(error**2)), 0.06849175638676988, places=12)
        self.assertEqual([float(values.min()), float(values.max())], [25.67, 29.36])

    def test_group_counts_and_source_id_mapping(self):
        result = recount()
        self.assertEqual((result['source_records'], result['groups'], result['selected_groups']), (47, 35, 6))
        self.assertEqual([c['groups'] for c in result['categories']], [27, 3, 2, 2, 1])
        self.assertEqual([c['selected'] for c in result['categories']], [3, 1, 1, 1, 0])
        with (ROOT / 'literature/source_records.csv').open(encoding='utf-8-sig') as h:
            sources = list(csv.DictReader(h))
        with (ROOT / 'literature/groups.csv').open(encoding='utf-8-sig') as h:
            groups = list(csv.DictReader(h))
        self.assertEqual(len({s['source_id'] for s in sources}), 47)
        for group in groups:
            expected = {v.strip() for v in group['source_evidence_ids'].split(';')}
            actual = {s['source_id'] for s in sources if s['group'] == group['group']}
            self.assertEqual(expected, actual)

    def test_nominal_supply_scope_and_distances(self):
        t = nominal_topology(ROOT / 'data/raw')
        self.assertEqual(t['network_counts'], {'junctions':782, 'reservoirs':2, 'tanks':1, 'pipes':905, 'pumps':1, 'valves':3})
        self.assertEqual(t['sectors']['C']['junctions'], 92)
        self.assertEqual(t['sectors']['C']['pressure_sensors'], ['n1', 'n4', 'n31'])
        self.assertEqual(t['sectors']['C']['AMR_count'], 82)
        self.assertEqual(t['feature_filter_counts'], {'all_channels':119, 'Area_C_and_pump_candidates':87, 'selected_signals':6})
        for name, expected in {'n1':891.3208, 'n4':573.7565, 'n31':307.7926}.items():
            self.assertAlmostEqual(t['T1_to_measured_pressure_nodes'][name]['distance_m'], expected, places=8)
        self.assertEqual([p['nominal_setting_m'] for p in t['PRVs']], [40, 50, 35])


if __name__ == '__main__':
    unittest.main()
