#Optimal O(n)
#Use hashmap

arr = [2,3,5,7]
target = 5
def findPairs(array, target):
  m1 = {} #store map on num in array to index

  for i, num in enumerate(array):
    diff = target - num

    if diff not in m1:
      m1[num] = i
    else:
      print(m1)
      return(m1[diff], i)

findPairs(arr, target)