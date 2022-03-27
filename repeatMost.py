# 2. Given an array of integers where all elements may repeat multiple times,
# write a method to determine which one of the elements repeats the most.
# Give consideration to performance.

def reMost(arr):
  dictt = {}
  for item in arr:
    dictt[item] = 1 + dictt.get(item,0)
  sortedDict = sorted(dictt.items(), key=lambda x : x[1], reverse=True)
  return sortedDict[0][0]

test = [1, 1, 2,2,2, 3, 4]
print(reMost(test))