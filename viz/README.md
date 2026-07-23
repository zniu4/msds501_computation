# vizlib

A small Python visualization library built on top of
[matplotlib](https://matplotlib.org/). It provides simple, reusable functions
for drawing charts and saving them as image files.

## What it does

Right now `vizlib` exposes a single function:

- `bar_chart(data, labels, title, output_path="bar_chart.png")` — draws a bar
  chart from your data and saves it as a PNG file. Returns the path to the
  saved file.

The library uses matplotlib's non-interactive `Agg` backend, so it works in
environments without a display (servers, CI, notebooks) and always saves the
result to disk.

## Project structure

```
viz/
├── vizlib/                  # library code
│   ├── __init__.py
│   └── charts.py            # bar_chart lives here
├── examples/                # runnable examples
│   └── bar_chart_example.py
├── tests/                   # tests
│   └── test_charts.py
├── requirements.txt         # dependencies
└── README.md                # this file
```

## Installation

From the `viz/` directory:

```bash
pip install -r requirements.txt
```

(Using a virtual environment is recommended.)

## Running the example

From the `viz/` directory:

```bash
python examples/bar_chart_example.py
```

This calls `bar_chart` with some fake fruit-sales data and writes
`fruit_sales.png` to the current directory. The script prints the absolute path
to the generated file when it finishes.

## Using it in your own code

```python
from vizlib import bar_chart

path = bar_chart(
    data=[10, 20, 30],
    labels=["Mon", "Tue", "Wed"],
    title="Daily Totals",
    output_path="daily.png",
)
print(f"Saved chart to {path}")
```

## Running the tests

From the `viz/` directory:

```bash
pytest tests/
```
