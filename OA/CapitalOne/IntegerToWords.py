'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


# O(1) O(1) cuz fixed
def numtoWord(num): 
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousand = 'Thousand Million Billion'.split()
    
    def word(num, idx=0):
        if num == 0:
            return []
        if num < 20:
            return [to19[num-1]]
        if num < 100:
            return [tens[num//10-2]] + word(num%10)
        if num < 1000:
            return [to19[num//100-1]] + ['Hundred'] + word(num%100)

        p, r = num//1000, num%1000
        if p % 1000 !=0: 
            space = [thousand[idx]] 
        else:
            space = []
        return  word(p, idx+1) + space + word(r)
    return ' '.join(word(num)) or 'Zero'

print(numtoWord(1232))
print(numtoWord(12345678))
print(numtoWord(1234567891))
