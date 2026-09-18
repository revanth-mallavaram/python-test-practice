import csv
import logging
from battery_rules import classify_voltage

with open("battery_results.log", "a") as log_file:
    log_file.write("\n")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", filename="battery_results.log", filemode="a")

LOW_THRESHOLD = 3.0
HIGH_THRESHOLD = 4.2

CRITICAL_LOW = 2.5
CRITICAL_HIGH = 4.5

pass_count = 0
fail_count = 0
error_count = 0
critical_count = 0

with open("battery_log.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        reading_id = row['reading_id']

        try:
            value = float(row['voltage_v'])
        except ValueError:
            error_count += 1
            logging.error(f"  Reading {reading_id}: bad value '{row['voltage_v']}'-- ERROR")
            continue
        result = classify_voltage(value)
        if result == "PASS":
            pass_count += 1
            logging.info(f"Reading {reading_id}: {value}C is between {LOW_THRESHOLD} and {HIGH_THRESHOLD} -- PASS")
        elif result == "CRITICAL":
            critical_count += 1
            logging.error(f"Reading {reading_id}: {value}C is outside {CRITICAL_LOW} - {CRITICAL_HIGH} ----- CRITICAL")
        else:
            fail_count += 1
            logging.warning(f"Reading {reading_id}: {value}C is outside {LOW_THRESHOLD} - {HIGH_THRESHOLD} ---- FAIL")
total_rows = pass_count + fail_count + error_count + critical_count
print(f"Total rows      : {total_rows}")
print(f"PASS            : {pass_count}")
print(f"FAIL            : {fail_count}")
print(f"ERROR (skipped) : {error_count}")
print(f"CRITICAL        : {critical_count}")