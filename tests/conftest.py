#!/usr/bin/env python3
"""
Pytest configuration for local imports.
"""

from __future__ import annotations

# Standard Library
import os
import sys

#============================================


def pytest_configure() -> None:
	repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
	if repo_root not in sys.path:
		sys.path.insert(0, repo_root)
