from sgp4.api import Satrec
from sgp4.api import jday
import numpy as np
import datetime

def propagate_object(name,line1,line2):

    satellite = Satrec.twoline2rv(line1,line2)

    now = datetime.datetime.utcnow()

    jd,fr = jday(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    error,pos,vel = satellite.sgp4(jd,fr)

    if error != 0:
        return None

    return name,np.array(pos),np.array(vel)


def propagate_many(objects):

    results=[]

    for name,l1,l2 in objects:

        r = propagate_object(name,l1,l2)

        if r is not None:
            results.append(r)

    return results