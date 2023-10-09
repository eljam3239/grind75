class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')', '{':'}','[':']'}
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i != mapping[a]:
                    return False
        return stack == []
 