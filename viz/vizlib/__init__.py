"""vizlib: a small matplotlib-based charting library.

Currently exposes:
    - bar_chart: draw a bar chart and save it as a PNG file.
"""

from .charts import bar_chart

__all__ = ["bar_chart"]
__version__ = "0.1.0"
