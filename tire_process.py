import csv
import logging
from tire_rules import classify_pressure, LOW_THRESHOLD, HIGH_THRESHOLD, CRITICAL_LOW, CRITICAL_HIGH

with open("tire_results.log", "a") as log_file:
    log_file.write("\n")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", filename="tire_results.log", filemode="a")

pass_count = 0
fail_count = 0
error_count = 0
critical_count = 0

with open("tire_log.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        reading_id = row['reading_id']

        try:
            value = float(row['pressure_psi'])
        except ValueError:
            error_count += 1
            logging.error(f"  Reading {reading_id}: bad value '{row['pressure_psi']}'-- ERROR")
            continue
        result = classify_pressure(value)
        if result == "PASS":
            pass_count += 1
            logging.info(f"Reading {reading_id}: '{row['position']}' with {value}PSI is between {LOW_THRESHOLD} and {HIGH_THRESHOLD} -- PASS")
        elif result == "CRITICAL":
            critical_count += 1
            logging.error(f"Reading {reading_id}: '{row['position']}' with {value}PSI is outside {CRITICAL_LOW} - {CRITICAL_HIGH} ----- CRITICAL")
        else:
            fail_count += 1
            logging.warning(f"Reading {reading_id}: '{row['position']}' with {value}PSI is outside {LOW_THRESHOLD} - {HIGH_THRESHOLD} ---- FAIL")
total_rows = pass_count + fail_count + error_count + critical_count
print(f"Total rows      : {total_rows}")
print(f"PASS            : {pass_count}")
print(f"FAIL            : {fail_count}")
print(f"ERROR (skipped) : {error_count}")
print(f"CRITICAL        : {critical_count}")