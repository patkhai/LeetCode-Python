
def decodeChar(letters):
    # res = ""
    # i = 0
    # while (i <= len(letters)-1):
    #     count = 1
    #     ch = letters[i]
    #     j = i
    #     while (j < len(letters)-1):
    #         if letters[j] == letters[j+1]:
    #             count += 1
    #             j += 1
    #         else:
    #             break
    #     res += str(count)+ch
    #     i = j+1
    # return res

    res = ""
    count = 0
    preChar = 0
    msg = []

    for ch in letters:
        if ch == preChar:
            count += 1
        else:
            if preChar != 0:
                res = str(count) + str(preChar)
                msg.append(res)
            preChar = ch
            count = 1
        res = str(count) + str(preChar)
    msg.append(res)
    return msg


letters = "aaaabbcc"
print(decodeChar(letters))
