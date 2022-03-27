# 1. Given a list of integers nums and an integer k,
# return the total number of continuous sublist whose sum equals to k

# brute force:
# double iteration. get each cont sublist. check if sum = k. if so increment count. edge cases: if lst is empty, print None. if no sublist sum = k, print 0
# time = O(n^2), space = constant
def sublist(lst, k):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            print(lst[i:j])
            if sum(lst[i:j]) == k:
                count += 1
    return count


print(sublist([1, 1, 1, 1], 2))


# print(sublist([10, 2, -2, -20, 10] , k = -10))
# print(contSublist([10, 2, -2, -20, 10] , k = -10))

# Linear time

def sublist1(lst, k):
    curSum = 0
    result = 0
    prefixDict = {0: 1}
    for num in lst:
        curSum += num
        diff = curSum - k
        prefixDict[curSum] = 1 + prefixDict.get(curSum, 0)
        result += prefixDict.get(diff, 0)

    return result


print(sublist1([1, 1, 1, 1], 2))
# initialize currentsum, result, and a dictionary of sum and counts starting with {0,1}.