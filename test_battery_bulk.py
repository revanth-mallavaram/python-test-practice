import csv
import pytest
from battery_logic import classify_voltage

def load_test_cases():   # NEW: reads the CSV, builds the same kind of tuple list you were typing by hand
    cases = []
    with open("battery_bulk.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            voltage = float(row['voltage_v'])
            expected = row['expected']
            cases.append((voltage, expected))
    return cases

@pytest.mark.parametrize("voltage, expected", load_test_cases())   # NEW: call the function instead of pasting a list
def test_classify_voltage(voltage, expected):
    assert classify_voltage(voltage) == expected