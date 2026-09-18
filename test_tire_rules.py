import pytest
from tire_rules import classify_pressure

@pytest.mark.parametrize("pressure, expected", [
    (32.0, "PASS"),
    (36.0, "CRITICAL"),
    (34.0, "PASS"),
    (31.9, "FAIL"),
    (36.1, "FAIL"),
    (25.0, "FAIL"),
    (40.0, "FAIL"),
    (9.1, "CRITICAL"),
    (24.9, "CRITICAL"),
    (49.1, "CRITICAL"),
    (40.1, "CRITICAL"),
])
def test_pressure_classification(pressure, expected):
    assert classify_pressure(pressure) == expected