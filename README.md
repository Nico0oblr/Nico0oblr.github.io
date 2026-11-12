# Nico S. Baßler — scientific website

Quarto source for <https://nico0oblr.github.io>, published through GitHub Pages.

## Edit locally or with Codex

All authored content lives in `site/`:

| File | Content |
| --- | --- |
| `site/index.qmd` | About and research interests |
| `site/publications.qmd` | Publications and preprints, with links to both versions |
| `site/notes/index.qmd` | Automatic research-note index |
| `site/notes/posts/*.qmd` | Individual notes |
| `site/code.qmd` | Public code links |
| `site/theme.scss` | Layout, colors, typography |
| `site/files/` | User-provided thesis PDFs |

Install [Quarto](https://quarto.org/docs/get-started/) (version 1.8.27 is used in CI). No Julia, Python packages, Node.js, or R installation is needed to render the initial content.

Preview with live reload:

```sh
quarto preview site --no-browser
```

Build the published files, including the search index:

```sh
python3 scripts/build.py
```

Inspect the result, then commit and push. GitHub Actions also renders source changes on `main`, commits the generated pages, and explicitly requests a Pages rebuild. GitHub Pages serves **main / (root)**, preserving the original repository's publishing route. No personal access token is required by the workflow.

Generated HTML, `site_libs/`, and related assets in the repository root are build output. Edit the `.qmd` source instead. `scripts/generated-files.json` records generated files so removed notes are also removed from the published output on the next build. Git history and previous deployments can still retain previously published content.

## Add a research note

1. Copy `site/_templates/research-note.qmd` to `site/notes/posts/a-descriptive-name.qmd`.
2. Fill in its title, description, date, categories, and content.
3. Remove `draft: true` when ready to include the page in the website.
4. Preview, build, and push. The note index and search update automatically.

This repository is public. `draft: true` excludes a document from the site build; it does **not** hide the source on GitHub. Keep confidential or unpublished working material outside this repository until intentionally shared.

Code blocks are displayed without execution by default. Add computational execution deliberately for a specific note when needed, and document its environment. For expensive simulations, link public code and include saved results.

## Useful Codex requests

- “Add this paper to Publications, preserving the author order and DOI.”
- “Turn this approved calculation into a research note; state its assumptions and link the source code.”
- “Build the site and check all internal links before committing.”

## Migration

The initial Quarto version replaces an uncustomized al-folio demo. The previous site remains in Git history at commit `3547552` and in the local `archive/pre-quarto-2026-11-12` branch. The original template's license is retained in `LICENSE`.
