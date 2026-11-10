# Social Tech Toolkit

The website lives in [`site/`](site/README.md). The research and content plan is in [`site-outline.md`](site-outline.md).

The [public case drafts](site/content/cases/articles.json) contain 72 examples needing editorial guidance. Read the [evidence guide](site/content/cases/evidence-guide.md), or browse http://localhost:4173/cases/ while the local server is running.

```sh
cd site
npm run build
npm test
npm run dev
```

Open http://localhost:4173. Deploy the generated `site/dist/` directory to a static host. See the website README for content editing, search behavior, and deployment configuration.
