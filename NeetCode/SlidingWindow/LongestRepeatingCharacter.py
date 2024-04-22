# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.
from collections import Counter


def charactersReplacement(s, k):
    max_len = 0
    max_count = 0
    scount = Counter()
    start = 0

    for end in range(len(s)):
        scount[s[end]] += 1
        max_count = max(max_count, scount[s[end]])

        replacementNeed = end - start + 1 - max_count

        if (replacementNeed) > k:
            scount[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len


s = "ABAB"
k = 2

print(charactersReplacement(s, k))


# max_length: This variable will store the maximum length of a valid substring containing the same character with at most k replacements.
# max_count: This variable will keep track of the maximum character count within the current window.
# char_count: This is a Counter object used to count character frequencies within the current window.
# start: This variable marks the left end of the sliding window.
# We iterate through the input string s using a sliding window approach. The variable end represents the current right end of the window.

# For each character at the end index:

# We increment the count of that character in char_count to keep track of its frequency.
# We update max_count to be the maximum count of any character within the window. This ensures that max_count represents the most frequently occurring character within the window.
# We check if the number of character replacements required within the current window exceeds the allowed limit k. This is determined by the condition (end - start + 1 - max_count) > k.

# If the condition is met, it means we need to shrink the window to make it valid. To do this, we:

# Get the character at the left end of the window using left_char.
# Decrement the count of left_char in char_count to account for its exit from the window.
# Move the left end of the window to the right by incrementing start.
# After each iteration, we update max_length with the maximum window length encountered so far.

# Finally, after processing the entire string, we return max_length, which represents the length of the longest valid substring containing the same character with at most k replacements. In the example provided, it's 4 for the input "ABAB" with k = 2.
