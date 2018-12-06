import re


def main():
    key_regex = re.compile(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d')
    file = open("input.txt", "r", encoding="utf-8")
    log = {}
    for row in file:
        row = row.rstrip()
        value = row[19:]
        key = key_regex.findall(row)
        log[key[0]] = value
    file.close()
    sorted_keys = sorted(log.keys())
    guard = 0
    id_regex = re.compile(r'#\d*')
    minute_dict = {}
    for i in range(0, len(sorted_keys)):
        guard_id = id_regex.findall(log[sorted_keys[i]])
        if len(guard_id) == 1:
            guard = guard_id[0][1:]
            if guard not in minute_dict:
                minute_dict[guard] = [0] * 60
        if log[sorted_keys[i]][0] == "f":
            asleep = int(sorted_keys[i][-2:])
        elif log[sorted_keys[i]][0] == "w":
            woke = int(sorted_keys[i][-2:])
            for j in range(asleep, woke):
                minute_dict[guard][j] += 1
    max = 0
    for guy in minute_dict:
        highest = sorted(minute_dict[guy], reverse=True)[0]
        if highest > max:
            max = highest
            my_man = guy
    index = minute_dict[my_man].index(max)
    print(int(my_man) * index)


main()
