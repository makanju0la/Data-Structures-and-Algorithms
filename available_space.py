# Find maximum of minimum of available hard disk space size found
# while analizing computer in segment of length x

#

# O(n^2)
def segment(x, space):
    lst = []
    for i in range(len(space)):
        for j in range(i + 1, len(space) + 1):
            sub = space[i:j]
            if len(sub) == x:
                lst.append(min(sub))
    return max(lst)


# O(n)
def segment(x, space):
    l = 0
    big = 0
    for r in range(len(space)):
        arr = space[l:r + 1]
        # print(arr)
        while r + 1 - l >= x:
            l += 1
        print(min(arr))
        big = max(big, min(arr))
    return big
    # Write your code here