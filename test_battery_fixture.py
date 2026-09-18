import csv
import pytest

@pytest.fixture(scope="module")
def battery_data():
    print("\n>>> FIXTURE RAN: opening the CSV")
    rows = []
    with open("battery_bulk.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def test_no_missing_voltages(battery_data):
    for row in battery_data:
        assert row['voltage_v'] != ""

def test_has_100_readings(battery_data):
    assert len(battery_data) == 100