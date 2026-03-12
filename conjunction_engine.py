import numpy as np

def compute_risk(pos1,pos2,vel1,vel2):

    distance = np.linalg.norm(pos1-pos2)

    relative_velocity = np.linalg.norm(vel1-vel2)

    return distance,relative_velocity