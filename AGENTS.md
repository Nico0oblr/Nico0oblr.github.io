# Website editing instructions

- Edit authored content in `site/`; root HTML and `site_libs/` are generated.
- Run `python3 scripts/build.py` after changes. Check navigation, internal links, and the relevant rendered pages before publishing.
- Use plain scientific language. Define rate conventions and assumptions in technical notes. Distinguish exact results, numerical evidence, and conjectures.
- Verify publication metadata against the journal or arXiv. Preserve author order. Do not invent affiliations, dates, ORCID identifiers, awards, contact details, or publication status.
- Verify presentation titles, dates, types, and presenter identity against the conference programme or user-provided information. A coauthor listing alone does not establish that the user presented. Add slides or poster files only when selected by the user for publication.
- Keep one entry per work and include separate Preprint and Published version links whenever available. Maintain the complete public paper list, including earlier work; update `site/publications.bib` alongside the page.
- This repository is public. Do not import private research, unpublished manuscripts, credentials, or local filesystem paths without explicit authorization for the specific material. `draft: true` does not make source private.
- Add notes under `site/notes/posts/`; the index and search are generated. Use the note template and update the date.
- Preserve `.nojekyll` and the existing `main` root publishing route. Source pushes trigger `.github/workflows/publish.yml`.
- Do not add dependencies or execute embedded scientific code unless needed for the requested change.
- Do not generate scientific figures or decorative research illustrations on the user's behalf unless explicitly requested. Use figures the user selects or supplies.
- Preserve user-requested content removals. Do not reintroduce removed scientific results or derivations without explicit authorization.
