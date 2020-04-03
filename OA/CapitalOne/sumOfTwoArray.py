'''
Given two array of characters, add them together like an addition problem and return them in a char array. ['3', '5', '9'] ['1', 2', '8', '4'] = 1284 + 359 = 1643 = ['1', '6', '4', '3']  

'''


def sumTwoArr(s1, s2):
    p = "".join(s1)
    t = "".join(s2)

    if p and t:
        total = int(p) + int(t)
        return list(str(total))


s1 = ["3", "5", "9"]
s2 = ["1", "2", "8", "4"]
print(sumTwoArr(s1, s2))  # ['1', '6', '4', '3']
