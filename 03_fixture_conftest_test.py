import pytest


# need to register in pytest.ini
@pytest.mark.user
def test_user(example_user):
    # To show the print output when running test:
    # pytest --capture=no     # show print statements in console
    # pytest -s               # equivalent to previous command
    print(example_user)
    assert example_user["name"] == "john"
    assert example_user["age"] == 13
