#Given a string with a word, return a string with all duplicates letter deleted.


# input -> banana
# output -> b
# Approach 1
def removeDuplicates(word):
    myDict = {}
    for ch in word:
        myDict[ch] = myDict.get(ch, 0) + 1
    print(myDict)
    for i in list(myDict):
        if myDict[i] > 1:
            del myDict[i]

    # sortedDict = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
    return (myDict)
# Time -> O(n)
# Space -> O(n)

#Approach 2
def removeDuplicates1(word):
  mySet = set(word)
  noDup = "".join(mySet)
  return(noDup)


