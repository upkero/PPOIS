## Laboratory Work: Library Sort and Spreadsort in Python

The project showcases two sorting algorithms implemented for generic Python objects:

- `LibrarySort` keeps a sparse "shelf" with gaps, expanding and rebalancing when the gaps become scarce.
- `SpreadSort` combines range partitioning with comparison sorting and recursively refines overloaded buckets.

### Project layout

- `LibrarySort.py` - class `LibrarySort` with the static method `sort`.
- `SpreadSort.py` - class `SpreadSort` with the static method `sort`.
- `Book.py` - class `Book`, a simple custom data type used in the demos.
- `SorterDemo.py` - class `SorterDemo` that runs several demonstrations.
- `Main.py` - class `Main`, the entry point that invokes the demos.

### Running the examples

Create and activate a virtual environment if needed, then execute:

```bash
python Main.py
```

The script prints the sorting results for integers, floating-point numbers, and the custom `Book` objects using both algorithms.

### Running the tests

The unit suite relies on `unittest` and the `coverage` package:

```bash
# optional: create and activate the virtual environment
python -m venv .venv
.venv\Scripts\python -m pip install coverage
.venv\Scripts\python -m coverage run -m unittest discover -s tests -p "*Tests.py"
.venv\Scripts\python -m coverage report
```

The current suite exercises every module and yields over 90% statement coverage.
