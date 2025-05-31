class ValidParenthesis:
    def is_valid(self, s: str) -> bool:
        matchBracket = {")":"(","]":"[",")":"("}
        stack = []
        for t in s :
            if t in matchBracket:
                #if t in matchBracket and stack[-1]== matchBracket[t]:
                if stack and stack[-1]== matchBracket[t]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(t)
        return True if not stack else False


if __name__ == "__main__":
    s = "()"
    s = "()[]{}"
    s = "(]"
   # s = "([])"
    res_obj = ValidParenthesis()
    result = res_obj.is_valid(s)
    print(result)