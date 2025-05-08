import pytest

def test_name_is_not_none():
    name = "Ashutosh"
    assert name is not None, "Name should not be None"

def test_name_value():
    name = "Ashutosh"
    assert name == "Ashutosh", f"Expected 'Ashutosh' but got {name}"

