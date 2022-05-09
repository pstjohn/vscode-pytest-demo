import pytest
from my_module.my_new_python_file import my_function


def test_true():
    assert True


def test_false():
    with pytest.raises(AssertionError):
        assert False


def test_my_function():
    assert my_function() == 5
