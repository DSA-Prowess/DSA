from typing import List, Optional
class EvalRpn:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a , b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[0]










if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    obj = EvalRpn()
    print(obj.evalRPN(tokens))