# Totesoft Legal Pages

This public repository hosts app-specific privacy, customer-terms, and support pages for Totesoft Atlassian Marketplace apps.

## Before publishing

1. Fill `PLACEHOLDER-VALUES.yml`.
2. Replace every matching token in the Markdown/YAML files.
3. Resolve all product and legal blockers in the external master checklist.
4. Obtain legal approval.
5. Remove each draft warning and `published: false` setting.
6. Run:

```bash
python3 scripts/check_placeholders.py .
```

7. Enable GitHub Pages from `main` and `/(root)`.

Do not use a draft page as a Marketplace privacy, terms, documentation, or support URL.
