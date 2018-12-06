
def main():
    file = open("input.txt", "r", encoding="utf-8")
    coords = []
    for row in file:
        row = row.rstrip()
        row = row.split(", ")
        coords.append([int(row[0]), int(row[1])])
    file.close()

    maxX = max(coords, key=lambda x: x[0])[0]
    maxY = max(coords, key=lambda y: y[1])[1]

    grid = []
    for i in range(0, maxX):
        grid.append([-1] * maxY)

    area = []
    for x in range(0, maxX):
        for y in range(0, maxY):
            total_distance = 0
            for pos in coords:
                delta_x = abs(pos[0] - x)
                delta_y = abs(pos[1] - y)
                total_distance += delta_x + delta_y
            if total_distance < 10000:
                area.append([x, y])
    print(len(area))


main()
