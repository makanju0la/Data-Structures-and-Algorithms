#Linear time
#Initialize sliding window deciding set, longest and left pointer. Iterate through string.
#use while loop to decide if to move leftmost character and slider. Otherwise, add
# current element to set, and return longest.
def longestSubLin(st):
    my_set = set()  # initialize set
    res = 0  # initialize longest
    left = 0  # initialize left pointer

    for right in range(len(st)):
        while st[right] in my_set: # Decide wether to move sliding window. Two things.
            # remove leftmost char from set and move slider to right
            my_set.remove(st[left])
            left += 1

        my_set.add(st[right])
        res = max(res, right - left + 1)

    return res


s = "abcabcbb"
print(longestSubLin(s))
