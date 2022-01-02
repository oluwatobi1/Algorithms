def isValid(s: str) -> bool:
    stack = []
    store = {")":"(", "]":"[", "}":"{"}
    # using stack approach 
    for i in s:
        if i in store.values():
            stack.append(i)
        else:
            if len(stack)>0 and stack[-1]==store[i]:
                stack.pop()
            else:
                return False
    return stack == []