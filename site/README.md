# Social Tech Toolkit

A static field guide to the ways people learn, cooperate, govern, share resources, and carry knowledge forward.

## Build and preview

Requires Python 3.10+ to build. Node 18+ is used only for the search tests and optional npm command shortcuts. There are no package dependencies or install step.

```sh
python3 scripts/build.py
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173. Equivalent shortcuts: `npm run build` and `npm run dev`.

```sh
npm test
```

Checks cover fuzzy and synonym ranking, invalid index data, generated links and anchors, sitemap coverage, and disabled search in initial HTML. Browser checks during development also cover loading after `window.load`, retry, malformed responses, mobile layouts, keyboard-compatible controls, accessibility, and browsing without JavaScript.

## Content

- `content/catalog.json`: 413 catalog records, publication flags, source codes, categories, descriptions, and use cases. All 413 entries have introductory source trails and are available in the local build.
- `content/scales.json`: six homepage groups from societies to everyday interactions, explicit primary placements, featured entries, and additional scales. The build checks that every published entry appears exactly once.
- `content/editorial.json`: expanded page content, aliases, and discovery terms for selected entries.
- `research/editorial/`: 408 provisional expanded articles, their linked sources and access notes. These override descriptions and article bodies for the remaining catalog entries; the five previously developed pages retain their content in `content/editorial.json`. See [the editorial handoff](research/editorial/README.md).
- `content/sources.json`: source links and provenance notes used on individual pages. References link directly to originals, inline where appropriate or in a local Sources section; there is no separate sources directory.
- `research/editorial/*-relations.json`: explicitly selected concept relationships and their editorial reasons. These drive “Explore alongside”; no alphabetical fallback is used. Internal links are written into the prose, not inserted through automatic keyword matching. `scripts/concept_links.py` validates coverage and ensures that every concept linked in an explanation also appears in its related list.
- `content/cases/articles.json`: 72 public case drafts with explicit editorial status and authored sections.
- `content/cases/evidence-guide.md`: the public explanation of how to interpret evidence.
- `research/cases/BACKLOG.md`: explicitly unresearched leads and priority evidence gaps.
- `scripts/cases.py`: validates a strict public schema and renders case articles with mandatory draft notices. It never reads or exports internal research dossiers. Cases link to technologies; matching technology pages link back.
- `research/cases/`: internal dossiers and historical report; never copied to public output.
- `research/README.md`: findings, limits, source access, and example situations for all 282 previously omitted entries.
- `research/baseline.json`: the original omission audit; the four topic files preserve the research records.
- `scripts/apply_research.py`: validates all 282 IDs and applies the research to the catalog, source registry, scale placements, report, and outline.
- `content/site-outline.md`: the research and planning document used for the initial import.
- `scripts/import_outline.py`: explicitly reimports the outline. This rebuilds catalog and source records, then reapplies the completed research batches; it is not part of the normal build.
- `templates/base.html`: shared page shell.
- `scripts/build.py`: homepage, entry, case-study, guide, search index, and sitemap generation.
- `assets/`: self-hosted CSS, SVG favicon, and dependency-free search.

To add an entry beyond the current inventory, add appropriate sources and editorial content, set `published` to `true`, assign its primary group in `scales.json`, and rebuild. Both the overview and search index use the same published records. Aliases are alternate names; discovery terms can link related ideas without implying equivalence. Edit curated metadata in `editorial.json`; the small shared vocabulary in `build.py` supplies additional common aliases.

## Search lifecycle

The input is visible and disabled in initial HTML. The index is fetched only after `window.load` (or immediately if the module initializes after load). The input is enabled only after the index is parsed, validated, and ready. Network or data failures keep it disabled and offer retry. Requests time out after 15 seconds. Browsing and all entry pages work without JavaScript.

The matcher normalizes case, accents, punctuation, and word order. It prioritizes exact titles and aliases, then title and alias prefixes, curated discovery terms, and conservative typo matches including transpositions. Short terms are not fuzzily expanded.

## Deployment

Upload `dist/` to any static host that serves directory `index.html` files. The repository also includes a Sites manifest for the registered private deployment. No server, database, CDN library, or external font is required. `404.html` and optional `_headers` are generated for compatible hosts.

`config.json` sets the current origin for canonical URLs and the sitemap. For another deployment:

```sh
SITE_URL=https://your-domain.example python3 scripts/build.py
```

Use an origin without a path prefix. Configuring DNS and attaching a custom domain are separate from building the site. The requested custom domain has not been attached; the current configuration uses the Sites deployment origin.

## Editorial scope

Source-backed does not mean experimentally validated. Pages distinguish practitioner methods, theories, and editorial adaptations. The 408 autonomous drafts carry a visible notice that they need further editorial guidance, and the homepage explains that the project uses AI and will change over time. Source access and remaining uncertainties are recorded alongside each draft. These notices do not imply that the five previously developed pages have received independent fact checking. The collection can expand without changing its architecture.
