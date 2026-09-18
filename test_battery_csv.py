import csv
import pytest

def load_test_cases():
    cases = []
    # your Week 2 code goes here:
    with open("battery_bulk.csv", "r") as file:#   - open the CSV
        reader = csv.DictReader(file)#   - DictReader it
        for row in reader:
            voltage = float(row['voltage_v'])
            expected = row['expected']#   - loop over rows
            cases.append((voltage, expected))#   - for each row, build a (voltage, expected) tuple and add it to cases
    return cases

@pytest.mark.parametrize("voltage, expected", load_test_cases())
def test_voltage_classification(voltage, expected):
    if voltage >= 3.0 and voltage <= 4.2:
        result = "PASS"
    elif voltage < 2.5 or voltage > 4.5:
        result = "CRITICAL"
    else:
        result = "FAIL"
    assert result == expected