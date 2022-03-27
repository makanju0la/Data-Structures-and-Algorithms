#new strategy. if length are unequal return false. if not, if there is ".",
#change it with the value at the position of string

def matchPattern(pattern, string):
  if len(pattern) != len(string):
    return False
  else:
    pattern, string = list(pattern), list(string)
    for i in range(len(pattern)):
      if pattern[i] == ".":
        pattern[i] = string[i]
    return True if pattern == string else False

matchPattern("....", "fooB")