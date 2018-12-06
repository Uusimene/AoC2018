def main():
    sum = 0
    sums = set([])
    sums.add(sum)
    flag = False
    while not flag:
        file = open("input.txt", "r", encoding="utf-8")
        for row in file:
            if flag:
                break
            sum += int(row.rstrip())
            print(sum)
            set_size = len(sums)
            sums.add(sum)
            if set_size == len(sums):
                flag = True

        file.close()
    print(sum)
    file.close()


main()
