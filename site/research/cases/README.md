# Case research catalog

Completed 6 November 2026: **72 case dossiers**, with **155 distinct source URLs** across 168 source records, linked to **128 toolkit entries**. These counts describe coverage, not independent confirmations. Four topic batches preserve the research records; the normal site build validates them and regenerates the report.

- [Read the full catalog](CATALOG.md).
- [Understand the evidence standards](EVIDENCE-GUIDE.md).
- [See further research leads](BACKLOG.md).
- Browse locally at http://localhost:4173/cases/.

## Coverage

| Batch | Cases | Focus |
| --- | ---: | --- |
| `gft-history-learning.json` | 18 | GFT-inspired institutional history, succession, learning, and contrasting evidence |
| `governance-commons.json` | 18 | Assemblies, participatory democracy, commons, treaties, and accountability |
| `prizes-open-production.json` | 18 | Prizes, open collaboration, cooperatives, credit, and incentives |
| `organizations-community.json` | 18 | LiquidO, Enspiral, microsolidarity, self-management, care, and community |

Fifteen dossiers contain explicit GFT manuscript references. Other cases extend or challenge its questions without being represented as examples from the book. GFT was read from the user-supplied manuscript; page references use printed manuscript numbering.

The first pass is institution-heavy: 39 institutional cases, 16 community cases, 12 society-scale cases, four group cases, and one movement case. Everyday arrangements need further research. The backlog explicitly preserves this gap rather than treating the current selection as exhaustive.

## Outcome and access notes

There are 50 mixed outcomes, eight failures on a stated objective, eight uncertain outcomes, and six bounded successes. These are editorial classifications of deliberately selected cases. They cannot establish a failure rate or compare technologies' effectiveness.

Source access: 99 relevant-section reviews, 32 search excerpts, 26 abstracts, and 11 full-text reviews. Restricted access is disclosed per source and in case limitations. Some external reports depend on participants' accounts; multiple URLs do not necessarily supply independent evidence. This is substantial exploratory research, not a systematic literature review or complete verification of every underlying dataset.

The evidence guide supplies cross-case research connections and a matrix of competing explanations. Each dossier separately records observations, hypotheses with alternatives, research status, practical questions, and remaining gaps. This makes later corrections possible without silently turning a tentative explanation into a fact.

## Editing and rebuilding

Edit the relevant batch JSON; keep stable case IDs and source IDs. `scripts/cases.py` validates source references, technology IDs, source-access categories, and case structure. Run from `site/`:

```sh
npm run build
npm test
```

The build creates `/cases/`, one page per dossier, an evidence guide, a research backlog, reciprocal technology links, and a downloadable `/case-catalog.json`. It also regenerates `CATALOG.md`. The existing technology search index remains focused on technology titles and keeps its load-after-window-load behavior.
