# CLAUDE.md

Guidance for working on the visualization library in this repository.

## Where the visualization library lives

The visualization library is contained entirely in the `viz/` subfolder:

- `viz/vizlib/` — library source code (the importable `vizlib` package).
- `viz/examples/` — runnable example scripts.
- `viz/tests/` — `pytest` test suite.

## Plotting rules

- All plotting **must** use [matplotlib](https://matplotlib.org/).
- The library **must** force the non-interactive `Agg` backend so charts can be
  saved as PNG files in environments without a display (servers, CI, notebooks).
  Set the backend *before* importing `pyplot`:

  ```python
  import matplotlib
  matplotlib.use("Agg")
  import matplotlib.pyplot as plt
  ```

## Adding a new chart function

Every new chart function requires all four of the following, in the same change:

1. **Implement it** in `viz/vizlib/charts.py`.
2. **Export it** from `viz/vizlib/__init__.py` (add it to the imports and to
   `__all__`).
3. **Add a runnable example** in `viz/examples/` that can be executed directly
   (e.g. `python examples/<name>_example.py` from the `viz/` directory) using
   fake/self-contained data.
4. **Add a matching `pytest` test** in `viz/tests/` that covers both the
   success path and the validation errors.

## Function requirements

- **Validate inputs.** Reject invalid arguments with a clear `ValueError`, e.g.
  empty data, or sequences whose lengths do not match. Do this before drawing.
- **Always close the figure handle.** Save inside a `try` and close the figure
  in a `finally` block so figures are never leaked across many calls, even when
  saving fails:

  ```python
  try:
      fig.savefig(output_path, dpi=150)
  finally:
      plt.close(fig)
  ```

## Generated output

- Generated PNG files are runtime artifacts and **must not be committed** to the
  repository. Do not add generated images to git.

## Before committing

- Run the test suite and make sure everything passes:

  ```bash
  cd viz
  pytest tests/
  ```
