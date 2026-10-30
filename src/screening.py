"""Recount the documented inventory supporting the student-directed focused review."""
import csv
from .data import ROOT

CATEGORIES = [('leak', 'Leak detection / localization'), ('state', 'Current-state estimation'),
              ('forecast', 'Pressure/head forecasting'), ('anomaly', 'Anomalies / sensor faults'),
              ('sensors', 'Sensor placement')]


def recount():
    with (ROOT / 'literature/source_records.csv').open(encoding='utf-8-sig', newline='') as handle:
        sources = list(csv.DictReader(handle))
    with (ROOT / 'literature/groups.csv').open(encoding='utf-8-sig', newline='') as handle:
        groups = list(csv.DictReader(handle))
    mapping = {group['group']: group for group in groups}
    assert len(mapping) == len(groups), 'Duplicate group identifier'
    assert {row['group'] for row in sources} == set(mapping), 'Inventory/group mismatch'
    for row in sources:
        assert row['category'] == mapping[row['group']]['category']
        assert row['selected'].lower() == mapping[row['group']]['selected'].lower()
    categories = []
    for key, label in CATEGORIES:
        selected = [g for g in groups if g['category'] == key]
        categories.append({'category': key, 'label': label, 'groups': len(selected),
                           'percent': 100*len(selected)/len(groups),
                           'selected': sum(g['selected'].lower() == 'true' for g in selected),
                           'group_ids': [g['group'] for g in selected]})
    assert sum(row['groups'] for row in categories) == len(groups)
    return {
        'source_records': len(sources), 'groups': len(groups),
        'selected_groups': sum(g['selected'].lower() == 'true' for g in groups),
        'categories': categories,
        'status': 'Reproduction of the documented inventory from the focused Milestone 2 review.',
        'attribution': 'Student-directed scope/filtering and critical review; AI-assisted discovery, categorization, code/source inspection, synthesis and counting.',
        'Ahmed_2025_in_historical_inventory': False,
        'limitation': 'Code verifies grouping and count consistency; source notes describe review coverage and scholarly classifications.',
    }
