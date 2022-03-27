
st = "()[]{]}"
def isValid(string):
    stack = []
    mapping = {']':'[',
               '}':'{',
               ')':'('}

    for s in string:
        if s in mapping:
            last_element = stack.pop() if stack else '#'
            if mapping[s] != last_element:
                return False
        else:
            stack.append(s)
    return True

print(isValid(st))

