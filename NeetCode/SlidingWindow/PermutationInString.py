# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
from collections import Counter


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1counter = Counter(s1)
    s2counter = Counter()

    for i in range(len(s2)):
        s2counter[s2[i]] += 1
        if i >= len(s1):
            if s2counter[s2[i - len(s1)]] == 1:
                del s2counter[s2[i - len(s1)]]
            else:
                s2counter[s2[i - len(s1)]] -= 1

        if s1counter == s2counter:
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))


# We import the Counter class from the collections module, which we'll use to count character frequencies.

# The checkInclusion function is defined, taking two input strings, s1 and s2.

# We check if the length of s1 is greater than the length of s2. If it is, we immediately return False because it's impossible for s2 to contain a permutation of s1 if s1 is longer.

# We initialize two Counter objects, s1_counter and s2_counter. s1_counter is filled with the counts of characters in s1, and s2_counter is initially empty. These counters will be used to keep track of character frequencies.

# We start a loop that iterates through each index i in the range from 0 to the length of s2. This loop will process each character in s2.

# Inside the loop, we increment the count of the character s2[i] in s2_counter. This keeps track of the character frequencies in the current sliding window.

# We check if the size of the sliding window has reached len(s1). If it has, it means we have a window of the same size as s1, so we need to adjust s2_counter accordingly.

# We handle the character that is exiting the sliding window (s2[i - len(s1)]):

# If the count of this character in s2_counter is 1, we delete it from the counter because it's no longer in the window.
# Otherwise, if its count is greater than 1, we decrement its count by 1 to reflect its new frequency within the window.
# We compare s1_counter and s2_counter at each iteration. If they are equal, it means the character frequencies in the sliding window of s2 match the frequencies in s1, indicating that a permutation of s1 is present in the current sliding window.

# If a matching permutation is found, we immediately return True.

# If the loop completes without finding a matching permutation, the function returns False because no permutation of s1 was found in s2.

# In summary, this code uses a sliding window approach along with character frequency counters to efficiently check if s2 contains a permutation of s1. It iterates through s2, updating the character frequencies as it goes, and checks for a match with the frequencies of s1. If a match is found, the function returns True; otherwise, it returns False.
