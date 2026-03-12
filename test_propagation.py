from tle_parser import parse_tle
from propagator_gpu import propagate_object

objects = parse_tle("../data/tle_cache.txt")

print("Loaded:", len(objects))

name, l1, l2 = objects[0]

print("Testing:", name)

result = propagate_object(name, l1, l2)

print(result)