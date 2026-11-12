# Expanded editorial drafts

This pass develops the 400 remaining catalog entries, including practices, organizational forms, systems, and social dynamics. Awards, Mentorship, Aristocracy, Markets, and Lobbying retain the text developed with the user. The 72 case studies are outside this writing pass.

Every new draft displays: **“AI-assisted draft — this page needs further editorial guidance.”** The homepage also identifies the project as developed with AI and subject to restructuring and editorial revision.

## What changed

Articles begin with a recognizable problem, possibility, or situation, explain the mechanism, and connect its difficulties to the same narrative. Examples are illustrative unless a linked source supports a named case. Subject-specific headings are optional; the removed generic sections have not been restored. References link directly from the prose, with a page-local Sources section only for additional references.

The four JSON batches are the editable source of these articles:

- `learning-community.json`: learning, relationships, participation, and community practices.
- `governance-work.json`: decisions, authority, collaboration, and organizational forms.
- `resources-succession.json`: resources, ownership, recognition, selection, and succession.
- `systems-dynamics.json`: larger systems and recurring social dynamics.

`manifest.json` records the exact scope and the five protected titles. Assignment files preserve the catalog material available at the beginning of this pass. `BRIEF.md` records the editorial instructions.

Completed coverage: 107 learning/community entries, 127 governance/work entries, 101 resources/succession entries, and 65 systems/dynamics entries. Together these contain approximately 83,200 words of article prose and 381 distinct source URLs. URL counts describe the source trail, not independent confirmations of the claims.

## Evidence and limits

This is an editorial expansion with targeted additional research, not a systematic review of 400 literatures. Each article records its source URLs, access level, provenance note, and research note. `existing-research-notes` means the previous catalog research was reused; it does not mean the full source was reread during this pass. `search-excerpt` and `abstract` likewise do not imply full-text access. Practitioner descriptions support explanations of a method, not general claims of effectiveness.

Additional research addressed gaps including public institutions, education, healthcare, ritual, extitutional theory, community arrangements, recognition, selection, and succession. Findings from particular experiments or historical settings remain bounded to those settings. Proposed examples and practical implications still need editorial judgment and, where consequential, deeper investigation.

## Continuing the editing

Edit `description`, `opening_html`, and optional `sections` in the appropriate batch. Keep inline citations and update source-access notes when further research changes the explanation. The build applies these bodies after the older catalog and editorial overlays. Editing only the catalog body will therefore not replace a draft.

The draft disclaimer is deliberately applied to every ID in this set. Finishing a copy edit does not automatically remove it. When an article has received the desired editorial guidance, explicitly update its status handling in `scripts/editorial_drafts.py`, the manifest, and the corresponding checks rather than silently dropping its draft record.

Build with `python3 scripts/build.py` from `site/`, then run `npm test`. Validation checks full batch coverage, required source metadata, inline citations, allowed markup, unique section anchors, the absence of the retired template headings, notices on the expected pages, internal links, the sitemap, and search behavior. These checks catch publishing mistakes; they do not establish that every substantive claim is correct.

## Classification correction

Athenian democracy was removed from the technology catalog after this writing pass. It exists only as the Athens case study, linked to democracy, assembly democracy, direct democracy, assemblies, sortition, elections, and jury trials. The current draft set contains 399 entries (64 systems/dynamics); the counts above document the original pass.

Private ownership (T340) was subsequently added as a linked concept for Capitalism, bringing the current draft set to 400 entries.

## Web of ideas — 7 November 2026

The 405 current catalog pages now have 668 distinct inline concept connections and 1,148 explicitly selected related-page connections. Each concept can be reached from at least one other concept's related list. These counts describe the completed linking pass and may change with later editing.

Links were chosen by reading the explanations, not generated from matching keywords. Some phrases were clarified to distinguish an ordinary action from a specific arrangement. External sources remain attached to their supporting claims; links to other catalog ideas lead to internal pages. The five previously developed articles received link corrections while retaining their narrative and structure.

The four batch `*-relations.json` files and `reviewed-relations.json` record a reason for each connection. The build requires explicit relationships for every published entry and rejects self-links, nested links, unknown concept destinations, and body links missing from “Explore alongside.” There is no category-based alphabetical fallback. A relationship need not be reciprocal, but selected return paths connect broader ideas with their concrete examples and alternatives.

## Intellectual property and innovation incentives — 8 November 2026

Added eight entries (T341–T348): Intellectual property, Patents, Copyright, Trade secrets, Advance market commitments, Commissioned research and development, Patent buyouts, and Earning from complementary capabilities. The catalog now has 405 entries, including 400 explicitly provisional drafts. Open licensing, Copyleft, and Prize competitions were updated to connect the new concepts; existing grants, contracts, confidentiality, and ownership relationships provide routes into the cluster.

The pages distinguish funding development, rewarding an achievement, supporting future purchases, and earning revenue after disclosure. AMCs can coexist with patents; grants do not inherently confer entrepreneurial upside; prizes do not automatically fund unsuccessful attempts or provide open access; and patent buyouts use existing rights before releasing them. Copyright is not presented as protection for an underlying technical idea.

WIPO supplies definitions and institutional distinctions. The Gavi AMC is an implemented example within the general explanation, not a newly added case dossier or a claim that all AMCs succeed. Patent buyouts are presented as a proposed mechanism with valuation difficulties. Complementary-capability evidence comes from a historical US manufacturing survey and is not generalized into a guaranteed business model. Direct NBER page access returned 403; available indexed abstracts/excerpts were used and recorded accordingly. The eight entries retain the editorial-guidance notice.
