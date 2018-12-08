

def main():
    file = open("input.txt", "r", encoding="utf-8")
    rules = {}
    for row in file:
        row = row.rstrip()
        if row[5:6] not in rules:
            rules[row[5:6]] = [row[36:37]]
        else:
            rules[row[5:6]].append(row[36:37])
            rules[row[5:6]].sort()

    file.close()
    walk(rules)


def walk(rules):
    keys = sorted(list(rules.keys()))
    available = set()
    order = []
    start = []

    for char in keys:
        first_flag = True
        for key in rules:
            if not first_flag:
                break
            if char in rules[key]:
                first_flag = False
        if first_flag:
            start.append(char)

    for item in start:
        available.add(item)
    available_list = sorted(available)
    current = available_list[0]
    available.remove(current)

    while len(order) != len(keys) + 1:
        order.append(current)
        try:
            for char in rules[current[0]]:
                available.add(char)
        except KeyError:
            break
        available_list = sorted(available)
        done = False
        for c in available_list:
            if done:
                break
            flag = True
            for key in rules:
                if not flag:
                    break
                if c in rules[key]:
                    if key not in order:
                        flag = False
            if flag:
                current = c
                available.remove(c)
                done = True
                break

    answer = ""
    for char in order:
        answer += char
    print(answer)


main()
