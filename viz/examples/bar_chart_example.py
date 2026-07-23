"""Runnable example: draw a bar chart with fake data using vizlib.

Run from the ``viz/`` directory:

    python examples/bar_chart_example.py

It will create ``fruit_sales.png`` in the current directory.
"""

import os
import sys

# Make the vizlib package importable when running this script directly,
# without needing to install the package first.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vizlib import bar_chart


def main() -> None:
    # Fake data.
    labels = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    data = [23, 45, 12, 37, 8]

    output_path = bar_chart(
        data=data,
        labels=labels,
        title="Fruit Sales (fake data)",
        output_path="fruit_sales.png",
    )

    print(f"Chart saved to: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    main()
