# ***********************************************************************************************************************
''''

)

1) 1. Two Sum
2) 9. Palindrome Number (Палиндромное число)
3) 13. Roman to Integer (От латинского к целому числу)
4) 14. Longest Common Prefix (Самый длинный распространенный префикс)
5) 20. Valid Parentheses (Допустимые  скобки)
100) 1491. Average Salary Excluding the Minimum and Maximum Salary(Средняя заработная плата без учета минимальной и максимальной зп)
'''
'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Учитывая массив целых чисел nums и целочисленное целевое значение, верните индексы двух чисел таким образом, чтобы они в сумме равнялись целевому значению.
Вы можете предположить, что каждый входной сигнал будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
Вы можете вернуть ответ в любом порядке.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
class Solution(object):
    def twoSum(self, arr, target):
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return None


nums = [3, 2, 4]
target = 6

obj = Solution()
print(obj.twoSum(nums, target))

#***********************************************************************************************************************
'''
9. Palindrome Number
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

# ***********************************************************************************************************************
'''
13. Roman to Integer (От латинского к целому числу)
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]

obj = Solution()
print(obj.romanToInt('XVII')) # 17

# ***********************************************************************************************************************
'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]
        return base


strs = ["flower", "flow", "flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))

# ***********************************************************************************************************************
'''
20. Valid Parentheses (Допустимые  скобки)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Дана строка s, содержащая только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка допустимой.
Входная строка допустима, если:
Открытые скобки должны быть закрыты скобками того же типа.
Открытые скобки должны быть закрыты в правильном порядке.
Каждая закрывающая скобка имеет соответствующую открытую скобку того же типа.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false'''


class Solution():
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


obj = Solution()
print(obj.isValid('(])'))  # False
print(obj.isValid('()[]{}'))  # True

#***********************************************************************************************************************
'''
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
Constraints:

Вам выдается массив уникальных целых чисел salary, где salary[i] - это зарплата i-го сотрудника.
Верните среднюю заработную плату сотрудников без учета минимальной и максимальной заработной платы. Будут приняты ответы в пределах 10-5 от фактического ответа.

Пример 1:
Входные данные: зарплата = [4000,3000,1000,2000]
Выход: 2500.00000
Пояснение: Минимальная и максимальная заработная плата составляют 1000 и 4000 долларов соответственно.
Средняя заработная плата без учета минимальной и максимальной составляет (2000+3000) / 2 = 2500

Пример 2:
Входные данные: зарплата = [1000,2000,3000]
Выход: 2000.00000
Пояснение: Минимальная и максимальная заработная плата составляют 1000 и 3000 долларов соответственно.
Средняя заработная плата без учета минимальной и максимальной составляет (2000) / 1 = 2000

'''
class Solution():
    def average(self, salary: list[int]) -> float:
        salary.sort()
        # return (sum(salary)-salary[0]-salary[-1])/(len(salary)-2)
        # return (sum(salary) - max(salary) - min(salary))/(len(salary)-2)
        return sum(salary[1:-1]) / (len(salary) - 2)


salary = [4000,3000,1000,2000]
obj = Solution()
print(obj.average(salary)) # 2500.0
#***********************************************************************************************************************
#***********************************************************************************************************************