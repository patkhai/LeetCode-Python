'''
def letterCombinations(digits):
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output


# O(n3)
def letterCombinations1(digits):
    if digits == "":
        return []

    nums_to_letters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    combs = [""]
    for digit in digits:
        new_combs = []
        for comb in combs:
            for letter in nums_to_letters[int(digit)]:
                new_combs.append(comb + letter)
        combs = new_combs

    return combs

'''

# O(n2)


def letterCombinations1(digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    if not digits:
        return []

    result = []

    if len(digits) == 1:
        return list(mapping[digits[0]])

    first_combination = mapping[digits[0]]
    last_combination = letterCombinations1(digits[1:])

    for elements in first_combination:
        for char in last_combination:
            result.append(elements+char)
    return result


digits = "7"
print(letterCombinations1(digits))


'''
created mapping for each number digits
if not digits, return empty
go through first digit combo in the mapping (in this case 2)
then go through last digit combo in the mapping (in this case 3)
once we have 2 list res combo
loop through first combo 
    loop through last combo
        add what is there to add in the result
return res (loop till it runs out of digits characters)


'''
