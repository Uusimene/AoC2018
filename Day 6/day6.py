
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

    for x in range(0, maxX):
        for y in range(0, maxY):
            closest_distance = -1
            closest = []
            for pos in coords:
                delta_x = abs(pos[0] - x)
                delta_y = abs(pos[1] - y)
                distance = delta_x + delta_y
                if closest_distance == -1 or closest_distance >= distance:
                    if closest_distance == distance:
                        closest.append(coords.index(pos))
                    else:
                        closest = [coords.index(pos)]
                    closest_distance = distance
            if len(closest) == 1:
                grid[x][y] = closest[0]

    areas = {}
    for i in range(0, len(coords)):
        areas[i] = 0
        for x in range(0, maxX):
            if areas[i] == -1:
                break
            for y in range(0, maxY):
                if areas[i] == -1:
                    break
                if grid[x][y] == i:
                    areas[i] += 1
                    if x == 0 or x == maxX - 1 or y == 0 or y == maxY - 1:
                        areas[i] = -1

    largest = list(sorted(areas.values(), reverse=True))
    print(largest[0])


main()
