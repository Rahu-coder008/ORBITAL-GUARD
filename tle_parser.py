def parse_tle(file_path):

    objects = []

    with open(file_path, "r") as f:

        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines) - 2, 3):

        name = lines[i]
        line1 = lines[i + 1]
        line2 = lines[i + 2]

        objects.append((name, line1, line2))

    return objects