from datetime import datetime


def main():

    startTime = datetime.now()
    file = open("input.txt", "r", encoding="utf-8")
    strings = []
    found = False
    for row in file:
        strings.append(row.rstrip())
    for id1 in strings:
        if found:
            break
        for id2 in strings:
            if found:
                break
            if id1 == id2:
                continue
            different = 0
            for x in range(0, len(id1)):
                if id1[x] != id2[x]:
                    different += 1
                    index = x
            if different == 1:
                correct_id1 = id1
                correct_id2 = id2
                found = True
    print(correct_id1)
    print(correct_id2)
    print(correct_id1[index])
    print(correct_id2[index])
    print(correct_id1[0:index]+correct_id1[index+1:])
    print(datetime.now() - startTime)


main()
