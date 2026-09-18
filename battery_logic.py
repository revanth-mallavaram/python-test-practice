import csv

def classify_voltage(voltage):
    LOW = 3.0
    HIGH = 4.2
    CRITICAL_LOW = 2.5
    CRITICAL_HIGH = 4.5

    if voltage >= LOW and voltage <= HIGH:
        return "PASS"
    elif voltage < CRITICAL_LOW or voltage > CRITICAL_HIGH:
        return "CRITICAL"
    else:
        return "FAIL"


if __name__ == "__main__":
    with open("battery_bulk.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            voltage = float(row['voltage_v'])
            result = classify_voltage(voltage)
            print(f"Reading {row['reading_id']}: {voltage}V -> {result}")