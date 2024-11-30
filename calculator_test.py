import pytest
from calculator import convert_test, trig_test, fact_test

# Тесты для convert_test
@pytest.mark.parametrize("num, base, expected", [
    (10, 2, "1010"),
    (255, 16, "FF"),
    (0, 2, "0"),
    (-10, 2, "-1010"),
])
def test_convert_test_positive(num, base, expected):
    assert convert_test(num, base) == expected

@pytest.mark.parametrize("num, base", [
    (10, 1),
    (10, -5),
    ("10", 2),
])
def test_convert_test_negative(num, base):
    with pytest.raises((ValueError, TypeError)):
        convert_test(num, base)

# Тесты для trig_test
@pytest.mark.parametrize("x, function_type, expected", [
    (0, "sin", 0.0),
    (90, "sin", 1.0),
    (0, "cos", 1.0),
    (45, "tg", pytest.approx(1.0, rel=1e-2)),
    (45, "ctg", pytest.approx(1.0, rel=1e-2)),
    (0, "ctg", float('inf')),
])
def test_trig_test_positive(x, function_type, expected):
    assert trig_test(x, function_type) == pytest.approx(expected, rel=1e-3) if expected != float('inf') else float('inf')

@pytest.mark.parametrize("x, function_type", [
    (90, "invalid"),
    ("90", "sin"),
])
def test_trig_test_negative(x, function_type):
    with pytest.raises(Exception):
        trig_test(x, function_type)

# Тесты для fact_test
@pytest.mark.parametrize("x, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_fact_test_positive(x, expected):
    assert fact_test(x) == expected

@pytest.mark.parametrize("x", [
    -1,
    "5",
])
def test_fact_test_negative(x):
    with pytest.raises((ValueError, TypeError)):
        fact_test(x)