'''
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution(object):
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
        l = []
        for i in s:
            if i in d.keys():
                l.append(i)
            else:
                if l == []:
                    return False
                if i != d[l.pop()]:
                    return False
        return l == []


obj1 = Solution()
print(obj1.isValid('(])'))