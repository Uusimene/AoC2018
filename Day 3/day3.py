def main():
    file = open("input.txt", "r", encoding="utf-8")
    claims = {}
    claim_count = 0
    claim_info = {}
    for row in file:
        claim_count += 1
        row = row.rstrip()
        xa = row.find("@") + 2
        xb = row.find(",")
        ya = xb + 1
        yb = row.find(":")
        wa = yb + 2
        wb = row.find("x")
        ha = wb + 1
        idb = row.find("@") - 1
        pos_x = int(row[xa:xb])
        pos_y = int(row[ya:yb])
        width = int(row[wa:wb])
        height = int(row[ha:])
        claim_id = int(row[1:idb])
        size = 0
        claim_info[claim_id] = [(pos_x, pos_y), (width, height)]
        for x in range(0, width):
            for y in range(0, height):
                try:
                    claims[(pos_x + x, pos_y + y)].append(claim_id)
                except KeyError:
                    claims[(pos_x + x, pos_y + y)] = [claim_id]
                size += 1
    file.close()

    for i in range(1, claim_count + 1):
        info = claim_info[i]
        to_remove = []
        flag = True
        for dx in range(0, info[1][0]):
            for dy in range(0, info[1][1]):
                try:
                    claims[(info[0][0] + dx, info[0][1] + dy)]
                except KeyError:
                    continue
                to_remove.append((info[0][0] + dx, info[0][1] + dy))
                if flag:
                    if len(claims[(info[0][0] + dx, info[0][1] + dy)]) > 1:
                        flag = False
        if not flag:
            for pos in to_remove:
                to_also_remove = []
                id_list = claims[pos]
                for id in id_list:
                    to_also_remove.append(claim_info[id][0])
                del claims[pos]
                for other_pos in to_also_remove:
                    try:
                        del claims[other_pos]
                    except KeyError:
                        continue

    values = list(claims.values())
    idd = values[0][0]
    w = claim_info[idd][1][0]
    h = claim_info[idd][1][1]
    while values.count([idd]) != w * h:
        for i in range(0, values.count([idd])):
            values.remove([idd])
        idd = values[0][0]
        w = claim_info[idd][1][0]
        h = claim_info[idd][1][1]

    print(values.count([idd]))


main()
