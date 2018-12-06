def main():
    file = open("input.txt", "r", encoding="utf-8")
    for row in file:
        polymer = row.rstrip()
    file.close()
    ready = False
    while not ready:
        flag = False
        for i in range(0, len(polymer) - 1):
            try:
                a = polymer[i]
                b = polymer[i + 1]
            except IndexError:
                continue
            if (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
                a = a.lower()
                b = b.lower()
                if a == b:
                    flag = True
                    polymer = polymer[0:i] + polymer[i + 2:]
        if not flag:
            ready = True
    print(len(polymer))


main()
