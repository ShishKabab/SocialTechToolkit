"""Apply the completed research batches; safe to rerun after importing the outline."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = {'learning-community': 79, 'governance-work': 93,
         'resources-succession': 86, 'systems-dynamics': 24}

def read(path):
    return json.loads((ROOT / path).read_text())

def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

research = []
for name, count in FILES.items():
    batch = read(f'research/{name}.json')
    assert len(batch) == count, (name, len(batch), count)
    research.extend(batch)
baseline = {e['id']: e for e in read('research/baseline.json')}
assert len(research) == len({r['id'] for r in research}) == len(baseline) == 282
assert {r['id'] for r in research} == set(baseline)
catalog = read('content/catalog.json')
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

report = ['# Research for the 282 previously unpublished entries', '',
          'All 282 entries in the omission audit now have a research record. The local site contains all 404 inventory entries. This is an introductory source pass, not a systematic evidence review.', '',
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

outline = (ROOT / 'content/site-outline.md').read_text()
lines = []
for line in outline.splitlines():
    match = re.match(r'\| ([TSD]\d{3}) \|', line)
    if match and match[1] in by_id:
        r = by_id[match[1]]
        cells = line.split('|')
        code = 'R-' + r['id']
        cells[-2] = ' ' + ('Adaptation: ' if r.get('adaptation') else '') + f'[{code}](#source-{code.lower()}) '
        if r.get('description'):
            cells[3 if r['id'].startswith('D') else 4] = ' ' + r['description'] + ' '
        line = '|'.join(cells)
    lines.append(line)
outline = '\n'.join(lines) + '\n'
outline = re.sub(r'\n<!-- research-sources-start -->.*?<!-- research-sources-end -->\n', '\n', outline, flags=re.S)
register = '\n<!-- research-sources-start -->\n' + '\n'.join(
    f'\n<a id="source-{code.lower()}"></a>\n{src["text"]}\n' for code, src in sorted(new_sources.items())) + '\n<!-- research-sources-end -->\n'
next_section = outline.index('\n## 10.')
outline = outline[:next_section] + register + outline[next_section:]
outline = re.sub(r'The breadth here exceeds the evidence depth\. \*\*282 entries remain marked C\*\*;[^\n]+',
                 'All 404 entries now have introductory source trails. The 282 previously marked C have individual research records with findings, limitations, access labels, and example situations in `site/research/README.md`. Evidence depth varies: some records rely on abstracts or search excerpts, and inclusion does not establish effectiveness. Full-text review, comparative evidence, and documented cases remain areas for further work.', outline)
outline = outline.replace('Search-result extracts were sufficient for discovery of some entries; full entry drafting still requires reading and checking the primary material.', 'Access levels are recorded explicitly. Entries supported only by abstracts or search excerpts remain introductory; deeper claims require full-text review.')
for path in (ROOT / 'content/site-outline.md', ROOT.parent / 'site-outline.md'):
    path.write_text(outline)
print(f'Applied {len(research)} records; {sum(e["published"] for e in catalog)} entries available locally.')
print('Access levels:', dict(Counter(r['access'] for r in research)))
