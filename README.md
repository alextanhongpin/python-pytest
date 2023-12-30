# python-pytest

## Print output
To show the print output when running test:


```bash
$ pytest --capture=no     # show print statements in console
$ pytest -s               # equivalent to previous command
```

## Disable requests

See `conftest.py`.

## Markers

Register your marker in `pytest.ini`.

Then add the marker to the test function:

```
@pytest.mark.my_marker
```

To invoke:

```
pytest -m my_marker
pytest -m "not my_marker"
```

To view all markers:

```
pytest --markers
```

## Coverage

We use `coverage.py` instead:

```bash
$ poetry add coverage
```

Run:
```bash
$ coverage run -m pytest
$ coverage report -m
$ coverage html
```
