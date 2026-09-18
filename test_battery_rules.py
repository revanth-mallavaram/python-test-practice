import pytest
from battery_rules import classify_voltage

@pytest.mark.parametrize("voltage, expected", [
    (3.0, "PASS"),
    (4.2, "PASS"),
    (2.5, "FAIL"),
    (4.5, "FAIL"),
    (2.9, "FAIL"),
    (4.3, "FAIL"),
    (2.4, "CRITICAL"),
    (4.6, "CRITICAL"),
])
def test_voltage_classification(voltage, expected):
    assert classify_voltage(voltage) == expected