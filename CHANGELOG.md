# Changelog

## 2.0.2

- Preserve signature image aspect ratios when scaling to form signature lines.

## 2.0.1

- Add Python 3.14 support metadata and CI coverage.
- Add regression tests for PDF merge/render, signature sizing, checkbox drawing, ID slot detection, and RTL text handling.
- Avoid a pypdf deprecation warning when merging overlays.
- Document GitHub private vulnerability reporting for sensitive security reports.

## 2.0.0

- Publish the import-only `pdf-form-tools` package to PyPI.
- Keep form-specific filling flows out of the reusable package.
