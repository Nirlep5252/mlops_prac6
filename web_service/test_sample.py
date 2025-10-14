import pytest


def test_simple_always_true():
    """A simple test that always returns true."""
    assert True


if __name__ == "__main__":
    pytest.main([__file__])
