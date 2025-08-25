class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                open_stack.append(c)
            else:
                if open_stack == []:
                    return False
                if c == ")" and open_stack[-1] != "(":
                    return False
                if c == "]" and open_stack[-1] != "[":
                    return False
                if c == "}" and open_stack[-1] != "{":
                    return False
                open_stack.pop()
        return True if open_stack == [] else False