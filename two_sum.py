#find pairs of numbers whose sum equal a target
#brute force

arr = [2,3,5,7]
target = 5
# return : (2,3), (2,5), (2,7), (3,5), (3,7), (5,7)

for i in range(len(arr)):
  for j in range(i+1, len(arr)):
    #print((arr[i],arr[j]))
    if sum((arr[i],arr[j])) == target:
      print((i,j))