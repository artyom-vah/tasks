#
# #***********************************************************************************************************************
# '''
# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Учитывая массив целых чисел nums и целочисленное целевое значение, верните индексы двух чисел таким образом, чтобы они в сумме равнялись целевому значению.
# Вы можете предположить, что каждый входной сигнал будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# '''
# class Solution(object):
#     def twoSum(self, arr, target):
#         for i in range(0, len(arr)):
#             for j in range(i + 1, len(arr)):
#                 if arr[i] + arr[j] == target:
#                     return [i, j]
#         return None
#
#
# nums = [3, 2, 4]
# target = 6
#
# obj = Solution()
# print(obj.twoSum(nums, target))
#
##***********************************************************************************************************************
'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''


class Solution(object):
    def isPalindrome(self, x):
        return False if x < 0 else str(x) == str(x)[::-1]


obj = Solution()
print(obj.isPalindrome(1221))

# #***********************************************************************************************************************
# '''
# 20. Valid Parentheses (Допустимые  скобки)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Дана строка s, содержащая только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка допустимой.
# Входная строка допустима, если:
# Открытые скобки должны быть закрыты скобками того же типа.
# Открытые скобки должны быть закрыты в правильном порядке.
# Каждая закрывающая скобка имеет соответствующую открытую скобку того же типа.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false'''
#
#
#
# class Solution(object):
#     def isValid(self, s: str) -> bool:
#         d = {'(': ')', '[': ']', '{': '}'}
#         l = []
#         for i in s:
#             if i in d.keys():
#                 l.append(i)
#             else:
#                 if l == []:
#                     return False
#                 if i != d[l.pop()]:
#                     return False
#         return l == []
#
#
# obj = Solution()
# print(obj.isValid('(])')) # False
# print(obj.isValid('()[]{}')) # True
# #***********************************************************************************************************************
