from datetime import datetime

alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    startTime = datetime.now()
    file = open("input.txt", "r", encoding="utf-8")
    for row in file:
        polymer = row.rstrip()
    file.close()
    shortest = 9999999999
    for letter in alphabet:
        test_poly = polymer.replace(letter, "")
        test_poly = test_poly.replace(letter.upper(), "")
        size = react(test_poly)
        if size < shortest:
            shortest = size
    print(shortest)
    print(datetime.now() - startTime)


def react(polymer):
    ready = False
    while not ready:
        flag = False
        for a in alphabet:
            startlen = len(polymer)
            polymer = polymer.replace(a+a.upper(), "")
            polymer = polymer.replace(a.upper()+a, "")
            if startlen > len(polymer):
                flag = True
        if not flag:
            ready = True
    return len(polymer)


main()
