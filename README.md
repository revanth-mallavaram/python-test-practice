# Python Test Practice

![Tests](https://github.com/revanth-mallavaram/python-test-practice/actions/workflows/tests.yml/badge.svg)

A learning repository for test automation — pytest, Bash scripting, and CI with GitHub Actions — applied to sensor pass/fail classification.

## What this does

Sensor readings are classified against specification thresholds into PASS, FAIL, CRITICAL, or ERROR. The classification logic is kept separate from the data processing so it can be unit tested directly, without files or logging involved.

## Structure

| File | Purpose |
|---|---|
| `tire_rules.py` | Classification logic and threshold constants — single source of truth |
| `tire_process.py` | Reads `tire_log.csv`, applies the rules, writes a timestamped log |
| `test_tire_rules.py` | Unit tests covering boundary values and edge cases |
| `run_tests.sh` | Runs the suite, generates an HTML report, gates processing on the result |
| `.github/workflows/tests.yml` | CI pipeline — runs on every push and on a nightly schedule |

## Running locally

```bash
pip install pytest pytest-html
bash run_tests.sh
```

Unit tests run first. If any fail, the script reports the failure and **skips data processing** rather than producing results from logic known to be broken. The HTML report lands in `reports/`.

## Specification

Tire pressure, in PSI:

| Range | Result |
|---|---|
| 32.0 – 36.0 | PASS |
| Below 25.0 or above 40.0 | CRITICAL |
| Outside normal but not critical | FAIL |
| Non-numeric value | ERROR — logged and skipped |

## CI

Every push runs the same script on a Linux runner. The HTML report is uploaded as a build artifact and retained against the commit that produced it — including when tests fail.