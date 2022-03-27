# 3. Longest Substring Without Repeating Characters
# Brute force.

# write helper function to check if substring is unique. iterate over string twice to get substrings.
# Let maxx = 0. for each substring, if unique, get new max(longest, len(substring)). return final max.
# s = "abcabcbb", ans = "abc" = 3
def uniqueCheck(st):
    return len(set(st)) == len(st)


def longestSub(st):
    longest = 0  # keep track of longest

    for i in range(len(st)):
        for j in range(i + 1, len(st) + 1):
            if uniqueCheck(st[i:j]):
                longest = max(longest, len(st[i:j]))

    return (longest)


# Time = O(n^2), Space = Constan time
s = "abcabcbb"
print(longestSub(s))


# Linear time
# Initialize sliding window deciding set, longest and left pointer. Iterate through string.
# use while loop to decide if to move leftmost character and slider. Otherwise, add current element to set, and return longest.
def longestSubLin(st):
    mySet = set()  # initialize set
    longest = 0  # initialize longest
    left = 0  # initialize left pointer

    for r in range(len(st)):
        while st[
            r] in mySet:  # Decide wether to move sliding window. Two things. remove leftmost char from set and move slider to right
            mySet.remove(st[left])
            left += 1

        mySet.add(st[r])
        longest = max(longest, r - left + 1)

    return longest


print(longestSubLin(s))