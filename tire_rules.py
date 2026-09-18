LOW_THRESHOLD = 32.0
HIGH_THRESHOLD = 36.0
CRITICAL_LOW = 25.0
CRITICAL_HIGH = 40.0

def classify_pressure(pressure):


    if pressure >= LOW_THRESHOLD and pressure <= HIGH_THRESHOLD:
        return "PASS"
    elif pressure < CRITICAL_LOW or pressure > CRITICAL_HIGH:
        return "CRITICAL"
    else:
        return "FAIL"