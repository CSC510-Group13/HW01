import pytest
from myfile import solve_quadratic


@pytest.fixture
def basic_quadratic():
    return (1, -5, 6)  # roots: 2, 3


@pytest.fixture
def one_root_quadratic():
    return (1, 2, 1)  # root: -1


@pytest.fixture
def complex_roots_quadratic():
    return (1, 0, 1)  # roots: i, -i


def test_two_real_roots(basic_quadratic):
    """Test quadratic equation with two distinct real roots."""
    a, b, c = basic_quadratic
    result = solve_quadratic(a, b, c)
    assert result == "Roots are: 3.0 and 2.0"


def test_one_real_root(one_root_quadratic):
    """Test quadratic equation with one real root (discriminant = 0)."""
    a, b, c = one_root_quadratic
    result = solve_quadratic(a, b, c)
    assert result == "One root: -1.0"


def test_complex_roots(complex_roots_quadratic):
    """Test quadratic equation with complex roots."""
    a, b, c = complex_roots_quadratic
    result = solve_quadratic(a, b, c)
    assert result == "Roots are: 0.0 + 1.0i and 0.0 - 1.0i"


def test_not_quadratic():
    """Test when a = 0 (not a quadratic equation)."""
    result = solve_quadratic(0, 2, 1)
    assert result == "Not a quadratic equation."


def test_float_coefficients():
    """Test with float coefficients."""
    result = solve_quadratic(1.5, -4.0, 2.0)
    assert "Roots are:" in result


def test_negative_discriminant():
    """Test with negative discriminant ensuring complex roots."""
    result = solve_quadratic(1, 0, 4)
    assert "Roots are: 0.0 + 2.0i and 0.0 - 2.0i" == result
