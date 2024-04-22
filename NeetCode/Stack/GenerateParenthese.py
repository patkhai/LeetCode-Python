# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

# add open paren if open < n 
# add a closing paren if closed < open 
# valif iif open == closed == n thats how we know the current combination is valid 

def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closed):
        if openN == closed == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN+1, closed)
            stack.pop()

        if closed < openN:
            stack.append(")")
            backtrack(openN, closed+1)
            stack.pop()

    backtrack(0, 0)
    return res


n = 3
print(generateParenthesis(n))

# The generateParenthesis function is defined, which takes an integer n as input and returns a list of all combinations of well-formed parentheses.

# Inside the generateParenthesis function, there's a stack list to keep track of the current combination of parentheses being built.

# The res list is used to store all valid combinations of well-formed parentheses.

# The backtrack function is defined to generate combinations. It takes two parameters:

# openN: This parameter represents the count of open parentheses added so far.
# closed: This parameter represents the count of closed parentheses added so far.
# Inside the backtrack function:

# If both openN and closed are equal to n, it means n pairs of parentheses have been added, and the current combination is valid. So, the combination stored in the stack is appended to the res list.

# If openN is less than n, it's valid to add an additional open parenthesis. The code appends "(" to the stack, increments openN by 1, and recursively calls backtrack with the updated values.

# If closed is less than openN, it's valid to add an additional closed parenthesis. The code appends ")" to the stack, increments closed by 1, and recursively calls backtrack with the updated values.

# The generateParenthesis function initializes the process by calling backtrack(0, 0) with both counts set to 0, indicating that no parentheses have been added initially.

# As the recursion unfolds, the backtrack function will add parentheses to the stack while ensuring that they are well-formed (the count of closed parentheses never exceeds the count of open parentheses). When a valid combination of n pairs of parentheses is reached, it is added to the res list.

# Once the recursion is complete, the generateParenthesis function returns the res list, which contains all the valid combinations of well-formed parentheses.
