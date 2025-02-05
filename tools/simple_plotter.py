def plot_points(file, skipFirstLine=False, width=40, height=20):
    coords = []
    with open(file, 'r') as file:
        lines = [line.split() for line in file]
        if skipFirstLine:
            lines = lines[1:]
        for line in lines:
            coords.append((float(line[0]), float(line[1])))

    min_x = min(x for x, y in coords)
    max_x = max(x for x, y in coords)
    min_y = min(y for x, y in coords)
    max_y = max(y for x, y in coords)

    scale_x = (max_x - min_x) / (width - 1) if max_x != min_x else 1
    scale_y = (max_y - min_y) / (height - 1) if max_y != min_y else 1

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for x, y in coords:
        px = int((x - min_x) / scale_x)
        py = int((y - min_y) / scale_y)
        py = height - 1 - py  # Flip y-axis for correct orientation
        grid[py][px] = '*'

    print("\n".join("".join(row) for row in grid))

plot_points('../files/tsp.txt', True)