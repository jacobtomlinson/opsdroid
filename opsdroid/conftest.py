"""Pytest config for all opsdroid tests."""
from opsdroid.testing import opsdroid, mock_api  # noqa: F401

from opsdroid.cli.start import configure_lang

__all__ = ["opsdroid"]

configure_lang({})
