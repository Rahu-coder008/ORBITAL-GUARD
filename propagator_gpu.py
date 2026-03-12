from sgp4.api import Satrec, jday
import numpy as np
import datetime


def propagate_object(name, line1, line2):

    try:

        # Clean lines
        line1 = line1.strip()
        line2 = line2.strip()

        if not line1.startswith("1") or not line2.startswith("2"):
            return None

        satellite = Satrec.twoline2rv(line1, line2)

        now = datetime.datetime.utcnow()

        jd, fr = jday(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second
        )

        error, position, velocity = satellite.sgp4(jd, fr)

        if error != 0:
            return None

        pos = np.array(position)
        vel = np.array(velocity)

        if not np.all(np.isfinite(pos)):
            return None

        if not np.all(np.isfinite(vel)):
            return None

        return name, pos, vel

    except Exception as e:

        print("Propagation error:", e)

        return None