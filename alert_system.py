def check_alert(distance):

    if distance < 10:
        return "CRITICAL"

    elif distance < 50:
        return "HIGH"

    elif distance < 100:
        return "MEDIUM"

    else:
        return "LOW"