# local_llm_wrapper

Local LLM wrapper with a simple, stable text-in text-out API. It supports multiple local backends (for example Ollama and Apple) via pluggable transports, with structured output helpers and robust parsing plus retry for unattended runs.

## Overview
- Library-first wrapper for local text models with a small, stable API.
- Fallback across transports when a backend is unavailable.
- Structured helpers for rename/sort workflows with strict parsing and format-fix retries.

## Features
- Pluggable transports in `local_llm_wrapper/transports/`.
- Fallback chain in `LLMEngine` with guardrail and context-window handling.
- Structured prompts and parsers for rename, keep, and sort workflows.
- Prompt sanitization and output normalization utilities.
- Quiet mode for non-verbose runs.

## Quick start
```python
from local_llm_wrapper.llm_engine import LLMEngine
from local_llm_wrapper.llm_utils import choose_model
from local_llm_wrapper.transports import AppleTransport, OllamaTransport

engine = LLMEngine(
	transports=[
		AppleTransport(),
		OllamaTransport(model=choose_model(None)),
	],
	quiet=True,
)

response = engine.generate("Say hello in one sentence.", max_tokens=120)
print(response)
```

## CLI example
```bash
python3 -c 'from local_llm_wrapper.llm_engine import LLMEngine; \
from local_llm_wrapper.llm_utils import choose_model; \
from local_llm_wrapper.transports import OllamaTransport; \
engine = LLMEngine(transports=[OllamaTransport(model=choose_model(None))], quiet=True); \
print(engine.generate("Say hello in one sentence.", max_tokens=80))'
```

## Structured helpers
The engine includes structured helpers for common file-organization tasks.

```python
from local_llm_wrapper.llm_engine import LLMEngine
from local_llm_wrapper.llm_prompts import SortItem
from local_llm_wrapper.transports import OllamaTransport

engine = LLMEngine(transports=[OllamaTransport(model="llama3.2:3b-instruct-q5_K_M")])
item = SortItem(path="notes.txt", name="notes", ext="txt", description="meeting notes")
result = engine.sort([item])
print(result.assignments)
```

## Transports
- Apple: `local_llm_wrapper/transports/apple.py`.
- Ollama: `local_llm_wrapper/transports/ollama.py`.
- Protocol: `local_llm_wrapper/transports/base.py`.

## Errors
Standardized exception types live in `local_llm_wrapper/errors.py` so callers can handle guardrails, context window errors, and transport availability consistently.

## Testing
- Pytest: `/opt/homebrew/opt/python@3.12/bin/python3.12 -m pytest tests`
- Pyflakes: `tests/run_pyflakes.sh`
- ASCII compliance: `/opt/homebrew/opt/python@3.12/bin/python3.12 tests/run_ascii_compliance.py`

## Docs
- Architecture: [docs/CODE_ARCHITECTURE.md](docs/CODE_ARCHITECTURE.md)
- File layout: [docs/FILE_STRUCTURE.md](docs/FILE_STRUCTURE.md)
- Changelog: [docs/CHANGELOG.md](docs/CHANGELOG.md)

## Notes
- This repo is text-only; image or OCR workflows belong elsewhere.
- Configuration is explicit through arguments or config objects, not custom environment variables.
