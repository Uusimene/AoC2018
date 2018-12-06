def main():
    file = open("input.txt", "r", encoding="utf-8")
    two = 0
    three = 0
    for row in file:
        dict = {}
        for char in row:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        two_bool = False
        three_bool = False
        for key in dict:
            if not two_bool:
                if dict[key] == 2:
                    two += 1
                    two_bool = True
            if not three_bool:
                if dict[key] == 3:
                    three += 1
                    three_bool = True
    file.close()
    print("Two: " + str(two) + " Three: " + str(three))
    print(str(two*three))


main()
