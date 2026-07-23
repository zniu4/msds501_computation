"""Tests for vizlib.bar_chart."""

import os
import sys

import pytest

# Make the vizlib package importable when running the tests directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vizlib import bar_chart


def test_bar_chart_creates_png(tmp_path):
    output = tmp_path / "chart.png"
    result = bar_chart(
        data=[1, 2, 3],
        labels=["a", "b", "c"],
        title="Test Chart",
        output_path=str(output),
    )

    assert result == str(output)
    assert output.exists()
    assert output.stat().st_size > 0


def test_bar_chart_mismatched_lengths():
    with pytest.raises(ValueError):
        bar_chart(data=[1, 2], labels=["only_one"], title="Bad")


def test_bar_chart_empty_data():
    with pytest.raises(ValueError):
        bar_chart(data=[], labels=[], title="Empty")
