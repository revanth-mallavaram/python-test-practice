#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)          # NEW: run the date command, store the result
REPORT="reports/report_$TIMESTAMP.html"   # NEW: build the filename, reusing the variable

echo "Starting tire pressure test suite..."
echo "Report will be saved to: $REPORT"   # NEW: show where it's going

mkdir -p reports                          # NEW: make the folder if it isn't there yet

python -m pytest test_tire_rules.py --html=$REPORT --self-contained-html -q   # NEW: added the report flags

EXIT_CODE=$?                          # NEW: capture the exit code IMMEDIATELY

if [ $EXIT_CODE -eq 0 ]; then         # NEW: if the code equals 0
    echo "RESULT: All tests passed."  # NEW
else                                  # NEW
    echo "RESULT: TESTS FAILED. See $REPORT"   # NEW
fi                                    # NEW: closes the if block

exit $EXIT_CODE      