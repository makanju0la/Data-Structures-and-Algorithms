# Input: s = "eceba"
# Output: 3
# Longest Substring with At Most Two Distinct Characters

def longestAtMostTwo(st):
    mySet = set()
    longest = 0  # Initialize
    left = 0

    for r in range(len(st)):
        mySet.add(st[r])
        while len(mySet) > 2:  # Decide when condition is broken
            mySet.remove(st[left])
            left += 1

            # Keep adding to set if condition is not broken
        longest = max(longest, r - left + 1)

    return longest


s = "eceba"
print(longestAtMostTwo(s))