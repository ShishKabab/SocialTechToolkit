"""Apply the completed research batches to the catalog and research records."""
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
FILES = ['learning-community', 'governance-work',
         'resources-succession', 'systems-dynamics']

def read(path):
    return json.loads((ROOT / path).read_text())

def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

research = []
for name in FILES:
    batch = read(f'research/{name}.json')
    research.extend(batch)
baseline = {e['id']: e for e in read('research/baseline.json')}
assert len(research) == len({r['id'] for r in research}) == len(baseline)
assert {r['id'] for r in research} == set(baseline)
catalog = read('content/catalog.json')
assert set(baseline) <= {e['id'] for e in catalog}, 'Research inputs must refer to current catalog entries'
sources = read('content/sources.json')
scales = read('content/scales.json')
groups = {g['id']: g for g in scales['groups']}
by_id = {r['id']: r for r in research}
new_sources = {}
for r in research:
    assert r['title'] == baseline[r['id']]['title'], r['id']
    for key in ('source_title', 'url', 'publisher', 'source_type', 'access',
                'finding', 'limitation', 'scenario', 'scale'):
        assert isinstance(r[key], str) and r[key].strip(), (r['id'], key)
    assert r['scale'] in groups and r['url'].startswith('https://'), r['id']
    assert isinstance(r['aliases'], list), r['id']
    r['reviewed_on'] = '2026-11-05'
    code = 'R-' + r['id']
    refs = [r, *r.get('additional_sources', [])]
    for ref in refs:
        ref['url'] = ref['url'].replace('(', '%28').replace(')', '%29')
    links = [{'title': ref['source_title'], 'url': ref['url']} for ref in refs]
    note = ' '.join(f'[{ref["source_title"]}]({ref["url"]}) — {ref["publisher"]}. '
                    f'{ref["source_type"]}; access: {ref["access"]}.' for ref in refs)
    new_sources[code] = {'text': f'**{code} — {r["title"]}.** {note}', 'links': links}
for e in catalog:
    if e['id'] not in by_id:
        continue
    r = by_id[e['id']]
    e['published'] = True
    e['research'] = r
    e['sources'] = list(dict.fromkeys([*e['sources'], 'R-' + e['id']]))
    e['adaptation'] = e['adaptation'] or r.get('adaptation', False)
    e['aliases'] = list(dict.fromkeys([*e['aliases'], *r['aliases']]))
    e['terms'] = list(dict.fromkeys([*e['terms'], *r.get('terms', [])]))
    if r.get('description'):
        e['description'] = r['description']
    for group in groups.values():
        group['entries'] = [i for i in group['entries'] if i != e['id']]
    groups[r['scale']]['entries'].append(e['id'])
sources.update(new_sources)
write('content/catalog.json', catalog)
write('content/sources.json', sources)
write('content/scales.json', scales)
write('research/remaining-entries.json', sorted(research, key=lambda r: r['id']))

report = ['# Research for retained entries from the original omission audit', '',
          f'{len(research)} retained entries have research records. The local site contains {len(catalog)} catalog entries. This is an introductory source pass, not a systematic evidence review.', '',
          'Access labels distinguish pages or sections reviewed, abstracts, and search excerpts. A method description is not evidence of effectiveness. Scenarios are editorial examples, not documented case studies. Sources checked on 2026-11-05.', '']
for category in dict.fromkeys(e['category'] for e in baseline.values()):
    subset = [r for r in research if baseline[r['id']]['category'] == category]
    report += [f'## {category} ({len(subset)})', '']
    for r in sorted(subset, key=lambda r: r['id']):
        report += [f'### {r["id"]} — {r["title"]}', '', r['finding'], '',
                   '**Limit:** ' + r['limitation'], '', '**Example situation:** ' + r['scenario'], '']
        for ref in [r, *r.get('additional_sources', [])]:
            report += [f'**Source:** [{ref["source_title"]}]({ref["url"]}) — {ref["publisher"]}. {ref["source_type"]}; **access:** {ref["access"]}.', '']
(ROOT / 'research/README.md').write_text('\n'.join(report))

print(f'Applied {len(research)} records; {sum(e["published"] for e in catalog)} entries available locally.')
print('Access levels:', dict(Counter(r['access'] for r in research)))
