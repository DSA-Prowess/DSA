class ValidParenthesis:
    def is_valid(self, s: str) -> bool:
        pass






if __name__ == "__main__":
    s = "()"
    s = "()[]{}"
    s = "(]"
    s = "([])"
    res_obj = ValidParenthesis()
    result = res_obj.is_valid(s)