def addparenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        elif c == ")" and len(stack) and stack[-1] == "(":
            stack.pop()
        elif c == "]" and len(stack) and stack[-1] == "[":
            stack.pop()
        elif c == "}" and len(stack) and stack[-1] == "{":
            stack.pop()
        else:
            return False
    return len(stack) == 0
    