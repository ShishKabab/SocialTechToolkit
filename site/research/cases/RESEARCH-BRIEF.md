# Case catalog research brief

Build an evidence-aware catalog of real cases, not recipes or success stories. User priorities: Great Founder Theory examples; LiquidO by Stelio Verzera; Enspiral and microsolidarity; Athens; prize failures including XPRIZE. Local research only, no deployment.

Write JSON array, one object per case:
- id: stable kebab-case; title; question (what someone could learn); period; location
- scale: one of societies/movements/institutions/communities/groups/everyday
- technology_ids: valid IDs in site/content/catalog.json (use exact mechanisms, not merely related words)
- summary: 40–70 words framing situation and arrangement
- outcome: success/mixed/failure/uncertain (scoped to the question, not a verdict on an entire society)
- outcome_summary: 30–60 words, what worked and what did not
- observations: 3–5 objects {claim,source_ids:[...]} documenting design/outcomes/limits; source-linked factual claims only
- hypotheses: 2–3 objects {claim,status,source_ids:[...],alternative}; status is supported-in-case / plausible / contested / participant-explanation. Explicitly separate causal inference from observations. Alternatives must be substantive, not generic disclaimers.
- theory_connections: 1–2 objects {theory,evidence_status,source_ids:[...],relevance,transfer_limit}. Name research/framework accurately; conceptual accounts and case evidence are not established causal laws. Primary scholarly research preferred. Do not manufacture a general theory connection; leave [] if none assessed and say so in research_gaps.
- lessons: 2–3 cautiously worded practical questions/inferences
- research_gaps: concrete unanswered questions, source access limits, selection/survivorship bias etc.
- sources: at least TWO substantive sources per case where available, objects {id,title,url,publisher,type,access,note}. URLs actually found/read. Access: full-text/sections/abstract/search-excerpt. Type distinguish participant-account/institutional-record/primary-research/review/history. Note what it supports and dependence on other sources.
- gft_reference: optional {chapter,pages,interpretation}; only if checked manuscript. GFT arguments are hypotheses, not independent validation.

Prefer several genuinely read sources over many title-only hits. Source word limits apply: keep source-derived prose concise, use your own hypotheses/examples, split broad reusable sources carefully. Aim ~250–450 words of analysis per case, not formulaic padding. Negative and mixed evidence especially valuable. If only one substantive source exists, keep case provisional (outcome uncertain), explain gap; do not fabricate independence. Distinguish implementation fidelity, immediate outputs, downstream adoption, sustainability and exclusion.

Keep shared project files unchanged. Each researcher writes only assigned batch JSON plus optional batch notes. Do not spawn agents. Save partial batches as you go. Validate technology IDs, source references, coverage and factual fit. Research ~18 substantial distinct cases per assigned batch; extra leads belong in separate optional leads array/file, not falsely complete cases.
