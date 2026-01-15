# Changelog

## 2026-01-15
- Add standardized LLM errors and transport-availability handling.
- Add quiet mode and a general text-only generate method.
- Add Apple transport instructions and retry support.
- Add Ollama transport history options with bounded turns and unreachable detection.
- Export the transport protocol alongside Apple and Ollama transports.
- Add pytest coverage for engine fallback and parse-retry behavior.
- Add architecture and file-structure documentation.
- Add a root-level `project.toml` with basic project metadata.
- Add notes summarizing the sibling OpenAI wrapper repo.
- Expand README with usage examples, testing, and docs pointers.
- Add a README CLI example for quiet `generate`.
- Expand pytest coverage for rename and sort flows.
- Add packaging files for PyPI builds (pyproject.toml, MANIFEST.in).
- Add pytest coverage for parsers and utilities.
- Add pip_requirements.txt for core dev/test dependencies.
- Add pytest coverage for prompt builders and utility helpers.
- Add pytest conftest to ensure local imports resolve when running tests directly.
- Remove the redundant `project.toml` now that `pyproject.toml` is the source of truth.
