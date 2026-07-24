"""Chart drawing functions for vizlib."""

from __future__ import annotations

from typing import Sequence

# Use a non-interactive backend so charts can be saved as files even when
# there is no display available (e.g. servers, CI).
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def bar_chart(
    data: Sequence[float],
    labels: Sequence[str],
    title: str,
    output_path: str = "bar_chart.png",
) -> str:
    """Draw a bar chart and save it as a PNG file.

    Args:
        data: The numeric height of each bar.
        labels: The label for each bar. Must be the same length as ``data``.
        title: The title shown at the top of the chart.
        output_path: Where to save the PNG file. Defaults to ``bar_chart.png``
            in the current working directory.

    Returns:
        The path to the saved PNG file.

    Raises:
        ValueError: If ``data`` and ``labels`` do not have the same length,
            or if ``data`` is empty.
    """
    if len(data) != len(labels):
        raise ValueError(
            f"data and labels must have the same length, "
            f"got {len(data)} and {len(labels)}"
        )
    if len(data) == 0:
        raise ValueError("data must not be empty")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, data, color="#4C72B0")
    ax.set_title(title)
    ax.set_ylabel("Value")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    fig.tight_layout()

    # Ensure the figure is always closed, even if saving fails, so we don't
    # leak figures across many calls.
    try:
        fig.savefig(output_path, dpi=150)
    finally:
        plt.close(fig)

    return output_path


def line_chart(
    x: Sequence[float],
    y: Sequence[float],
    title: str,
    xlabel: str = "x",
    ylabel: str = "y",
    output_path: str = "line_chart.png",
) -> str:
    """Draw a line chart and save it as a PNG file.

    Args:
        x: The x-coordinate of each point.
        y: The y-coordinate of each point. Must be the same length as ``x``.
        title: The title shown at the top of the chart.
        xlabel: The label for the x-axis. Defaults to ``"x"``.
        ylabel: The label for the y-axis. Defaults to ``"y"``.
        output_path: Where to save the PNG file. Defaults to ``line_chart.png``
            in the current working directory.

    Returns:
        The path to the saved PNG file.

    Raises:
        ValueError: If ``x`` and ``y`` do not have the same length, or if
            ``x`` is empty.
    """
    if len(x) != len(y):
        raise ValueError(
            f"x and y must have the same length, got {len(x)} and {len(y)}"
        )
    if len(x) == 0:
        raise ValueError("x must not be empty")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color="#4C72B0", marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()

    # Ensure the figure is always closed, even if saving fails, so we don't
    # leak figures across many calls.
    try:
        fig.savefig(output_path, dpi=150)
    finally:
        plt.close(fig)

    return output_path
