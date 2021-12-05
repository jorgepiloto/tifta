"""Holds a plethora of tests for checking TIFTA package metadata."""

import tifta


def test_tifta_version():
    assert tifta.__version__ == "0.1.dev0"
