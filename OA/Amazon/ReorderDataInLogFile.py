def sortBoxes(logs):
    res1, res2 = [], []

    for item in logs:

        if item.split()[1].isdigit():
            res2.append(item)
        else:
            res1.append(item.split())

    res1.sort(key=lambda x: x[0])
    res1.sort(key=lambda x: x[1:])

    for i in range(len(res1)):
        res1[i] = " ".join(res1[i])

    res1.extend(res2)

    return res1


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(sortBoxes(logs))

