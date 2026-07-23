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
