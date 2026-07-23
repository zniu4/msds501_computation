"""Runnable example: draw a line chart with fake data using vizlib.

Run from the ``viz/`` directory:

    python examples/line_chart_example.py

It will create ``monthly_temp.png`` in the current directory.
"""

import os
import sys

# Make the vizlib package importable when running this script directly,
# without needing to install the package first.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vizlib import line_chart


def main() -> None:
    # Fake data.
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    temps = [4, 6, 11, 16, 21, 25, 28, 27, 22, 15, 9, 5]

    output_path = line_chart(
        x=months,
        y=temps,
        title="Average Monthly Temperature (fake data)",
        xlabel="Month",
        ylabel="Temperature (°C)",
        output_path="monthly_temp.png",
    )

    print(f"Chart saved to: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    main()
