#Find and Replace Pattern
#helper function: Takes a word and a pattern. If word matches pattern returns true otherwise false

def match(word, pattern):
  m1 = {}
  m2 = {}

  for w, p in zip(word, pattern):
    if w not in m1:
      m1[w] = p
    if p not in m2:
      m2[p] = w
    if (m1[w], m2[p]) != (p,w):
      return False
  return(True)

match("a", "x")

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
filteredWords = [w for w in words if match(w, pattern)]
print(filteredWords)