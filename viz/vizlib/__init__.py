"""vizlib: a small matplotlib-based charting library.

Currently exposes:
    - bar_chart: draw a bar chart and save it as a PNG file.
    - line_chart: draw a line chart and save it as a PNG file.
"""

from .charts import bar_chart, line_chart

__all__ = ["bar_chart", "line_chart"]
__version__ = "0.1.0"
