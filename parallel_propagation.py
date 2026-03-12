from multiprocessing import Pool, cpu_count
from propagator_gpu import propagate_object


def wrapper(obj):

    name, line1, line2 = obj

    return propagate_object(name, line1, line2)


def propagate_many(objects):

    workers = cpu_count()

    print("Using", workers, "CPU cores for propagation")

    with Pool(workers) as pool:

        results = pool.map(wrapper, objects)

    results = [r for r in results if r is not None]

    return results