def suggest_maneuver(distance):

    if distance < 10:
        return "Perform orbit raise maneuver"

    elif distance < 50:
        return "Adjust inclination"

    else:
        return "No maneuver needed"