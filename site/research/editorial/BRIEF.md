# Autonomous editorial research brief

User explicitly requests development of ALL remaining technologies, with extra research where necessary and an editorial-guidance disclaimer. Local only. The Sites skill permits bounded research delegation. Each assigned batch is a bounded research-and-explanation task; root owns integration and disclaimers. Do not spawn more agents or edit shared site files.

Read your `*-assignment.json`, existing research in `site/research/`, catalog/source registry, and the user-developed Awards, Mentorship, Aristocracy, Markets, and Lobbying HTML for editorial judgment. Preserve those five pages. Do not assume existing descriptions are correct if research contradicts them.

## Deliverable

Write `site/research/editorial/BATCH.json` as an ARRAY, one record for EVERY assigned ID, progressively saved in groups. Do not put completed drafts into the assignment file.

Record schema:
```
{
 "id":"T...", "title":"Exact catalog title",
 "description":"Clear inviting one-sentence explanation, about 15–30 words",
 "opening_html":"<p>Coherent concrete opening explaining why this matters...</p>",
 "sections":[{"id":"specific-kebab-id","title":"Subject-specific heading","html":"<p>...</p>"}],
 "sources":[{"title":"Actual source title","url":"https://...","access":"sections / abstract / search-excerpt / existing-research-notes / full-text","note":"What was reviewed and what it supports; distinguish current browsing from existing research"}],
 "research_note":"Brief internal editorial/research limitations, missing evidence, conceptual boundaries; never claim full text read if not",
 "reviewed_on":"2026-11-06"
}
```
All reader-facing source references should be direct inline links. Existing verified links can be retained after reviewing the relevant local research notes; this is NOT a claim to have freshly read the original. Browse for missing, niche, uncertain, medical/legal, or contested claims and when the notes are insufficient. Add substantive fresh research where warranted rather than browsing mechanically once per concept. Never invent URLs, outcomes, quotations, historical examples, or consensus. Prefer primary research and original practitioner descriptions. Source word limits apply across the batch; avoid drawing dozens of entries from one 200-word-limited source.

## Editorial standard

- Explain a social mechanism that changes what people can accomplish. Start with its importance or an understandable situation. Public audience: not aimed at software insiders.
- Each paragraph should follow from the previous one. No universal structure. Use 0–3 topic-specific sections as useful. Develop most entries to ~200–350 words; shorter simple practices can be ~160–220, larger systems may need 400+. Do not pad to a target or stretch an obscure term into a proven theory.
- Write each entry individually. NO generating prose from category templates, shared opening/closing sentences, phrase banks, or mechanically expanding existing findings. No copies with nouns swapped. Code can serialize individually composed prose.
- Preserve genuine differences among similar entries (e.g. advice vs consent; funding vs ownership). Discuss meaningful boundaries naturally in the explanation, not a pile of caveats.
- Explain directly. Avoid “Author X argues…”, “this source describes…”, “the paper illustrates…”. Put attribution in links. Historical attribution is fine when it explains the origin, but don't narrate source material.
- Use concrete, varied, clearly hypothetical examples. Do not carry the cooking example into these pages. Do not invent personal experiences. Named real cases require specific evidence and can link to existing `/cases/.../` if genuinely relevant.
- Integrate difficulties into the narrative: what breaks, who can be excluded, what hidden work makes the arrangement possible. Avoid generic 'not guaranteed' warnings or moralizing.
- No stock sections named “How it works”, “In practice”, “Conditions & tradeoffs”, “When to use it”, or “Sources & further reading”. No ending that simply says ask questions, clarify goals, monitor results. No 'In short', 'Bottom line', 'leverage', 'empower'.
- No link arrow icons. No separate /sources/ links or source-code references. Use descriptive inline links attached to relevant phrases; bibliography fallback is root's responsibility.
- Keep HTML simple: p, a, strong, em, occasional ul/ol/table only when useful. Escape ampersands in hrefs as &amp;. Use stable source URLs. Do not include h1/h2 or script/style in body; headings provided by sections.
- Build a web of ideas: when another catalog concept does explanatory work, link that phrase to its internal page. Keep the external source on the supported claim or verb instead of using the concept name as the citation. Do not link every occurrence or substitute a vaguely related concept for the words actually used. If a connection needs explanation, make the relationship explicit in a short natural sentence.
- Maintain the batch's `*-relations.json` alongside the prose. Choose components, complements, alternatives, or relevant dynamics for “Explore alongside,” with a specific editorial reason for each. Include every concept linked in the article body. Category membership and alphabetical order are not reasons for a relationship. The five user-developed pages can receive link-only corrections without rewriting their explanations.
- Dynamic phenomena are lenses, not tools to prescribe blindly. Broad domains are not single recipes. Expose internal components and realistic tradeoffs.
- Root adds “AI-assisted draft — this page needs further editorial guidance.” Don't repeat disclaimer in content.

Save partial progress frequently. Validate IDs, nonempty bodies, source links, and unique section IDs. Report completion counts, fresh sources, and unresolved substantive limitations. Root will review samples and integrate all records, rather than mistaking coverage for fact-checking completeness.
