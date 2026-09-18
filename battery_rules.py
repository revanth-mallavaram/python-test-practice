def classify_voltage(voltage):
    LOW_THRESHOLD = 3.0
    HIGH_THRESHOLD = 4.2
    CRITICAL_LOW = 2.5
    CRITICAL_HIGH = 4.5

    if voltage >= LOW_THRESHOLD and voltage <= HIGH_THRESHOLD:
        return "PASS"
    elif voltage < CRITICAL_LOW or voltage > CRITICAL_HIGH:
        return "CRITICAL"
    else:
        return "FAIL"