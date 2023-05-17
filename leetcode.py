# ***********************************************************************************************************************
''''
1) 1. Two Sum
2) 9. Palindrome Number (Палиндромное число)
3) 13. Roman to Integer (От латинского к целому числу)
4) 14. Longest Common Prefix (Самый длинный распространенный префикс)
5) 20. Valid Parentheses (Допустимые  скобки)
6) 26. Remove Duplicates from Sorted Array (Удалить дубликаты из отсортированного массива)
7) 27. Remove Element (Удалить элемент)
8) 28. Find the Index of the First Occurrence in a String (Найдите индекс первого вхождения в строку)
9) 35. Search Insert Position (Поиск позиции вставки)
10) 58. Length of Last Word (Длина последнего слова)
11) 66. Plus One
12) 67. Add Binary
13) 69. Sqrt(x)
14) 70. Climbing Stairs (Поднимаясь по лестнице)
15) 83. Remove Duplicates from Sorted List (Удалить дубликаты из отсортированного списка)
16) 88. Merge Sorted Array (Объединить отсортированный массив)
17) 100. Same Tree (То же дерево)
18) 101. Symmetric Tree (Симметричное дерево)
19) 108.Convert Sorted Array to Binary Search Tree (Преобразование отсортированного массива в двоичное дерево поиска)
20) 110. Balanced Binary Tree (Сбалансированное бинарное дерево)
21) 111. Minimum Depth of Binary Tree (Минимальная глубина бинарного дерева.)
22) 112. Path Sum
23) 118. Pascal's Triangle
24) 119. Pascal's Triangle II
25) 121. Best Time to Buy and Sell Stock (Лучшее время для покупки и продажи акций)
26) 125. Valid Palindrome
27) 136. Single Number


101) 1491. Average Salary Excluding the Minimum and Maximum Salary(Средняя заработная плата без учета минимальной и максимальной зп)
102) 2678. Number of Senior Citizens (Количество пожилых граждан)

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

# ***********************************************************************************************************************
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
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]


obj = Solution()
print(obj.romanToInt('XVII'))  # 17

# ***********************************************************************************************************************
'''
14. Longest Common Prefix (Самый длинный распространенный префикс)
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Напишите функцию для поиска самой длинной строки общего префикса среди массива строк.
Если общего префикса нет, верните пустую строку "".

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
print(obj.longestCommonPrefix(strs))  # fl

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

# ***********************************************************************************************************************
'''
26. Remove Duplicates from Sorted Array (Удалить дубликаты из отсортированного массива)
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:
The judge will test your solution with the following code:

Учитывая целочисленный массив nums, отсортированный в порядке неубывания, удалите дубликаты на месте таким образом,
чтобы каждый уникальный элемент появлялся только один раз. Относительный порядок элементов должен быть сохранен неизменным. 
Затем верните количество уникальных элементов в nums. Считайте, что количество уникальных элементов nums равно k, чтобы 
быть принятым, вам нужно выполнить следующие действия:
Измените массив nums таким образом, чтобы первые k элементов nums содержали уникальные элементы в том порядке, в котором 
они присутствовали в nums изначально. Остальные элементы nums не важны так же, как и размер nums.
Верните k.
Судья по обычаю:
Судья протестирует ваше решение с помощью следующего кода:

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


################## *** Вариант 1 *** ##################
class Solution():
    def removeDuplicates(self, nums):
        # return len(set(nums))
        replace = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicates(nums))


################## *** Вариант 2 *** ##################
class Solution():
    def removeDuplicates(self, nums):
        first = 0
        second = 0
        while second < len(nums):
            while second < len(nums) - 1 and nums[second] == nums[second + 1]:
                second += 1
            nums[first] = nums[second]
            first += 1
            second += 1
        return len(nums[:first])


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1,1,2]
obj = Solution()
print(obj.removeDuplicates(nums))

# ***********************************************************************************************************************
'''
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order 
of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following 
things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Учитывая целочисленный массив nums и целое значение val, удалите все вхождения val в nums на месте. Порядок
элементов может быть изменен. Затем верните количество элементов в nums, которые не равны val.
Учтите, что количество элементов в nums, которые не равны val, равно k, чтобы их приняли, вам нужно выполнить следующие
действия:
Измените массив nums таким образом, чтобы первые k элементов nums содержали элементы, которые не равны val.
Остальные элементы nums не важны так же, как и размер nums.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Объяснение: Ваша функция должна возвращать k = 2, причем первые два элемента nums равны 2.
Не имеет значения, что вы оставляете за пределами возвращаемого k (следовательно, они являются символами подчеркивания).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
Объяснение: Ваша функция должна возвращать k = 5, причем первые пять элементов nums содержат 0, 0, 1, 3 и 4.
Обратите внимание, что пять элементов могут быть возвращены в любом порядке.
Не имеет значения, что вы оставляете за пределами возвращаемого k (следовательно, они являются символами подчеркивания).
'''


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


nums = [0, 1, 3, 4, 3]
val = 3
o = Solution()
print(o.removeElement(nums, val))

# ***********************************************************************************************************************
'''
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Учитывая две строки игла и стог сена, вернуть индекс первого вхождения иглы в стог сена или -1, если игла не является частью стога сена.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))

# ***********************************************************************************************************************
'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Учитывая отсортированный массив различных целых чисел и целевое значение, вернуть индекс, если цель найдена. Если нет,
верните индекс туда, где он был бы, если бы он был вставлен по порядку. 
Вы должны написать алгоритм со сложностью выполнения O(log n).

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


arr = [1, 3, 5, 6]
t = 2
obj = Solution()
print(obj.searchInsert(arr, t))

# ***********************************************************************************************************************
'''
58. Length of Last Word 
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Для заданной строки s, состоящей из слов и пробелов, вернуть длину последнего слова в строке. 
Слово – это максимальная подстрока состоящая только из не пробельных символов.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"

Output: 6
Explanation: The last word is "joyboy" with length 6.
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


s1 = "   fly me   to   the moon  "
obj = Solution()
print(obj.lengthOfLastWord(s1))  # 4

# ***********************************************************************************************************************
'''
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''


################## *** Вариант 1 *** ##################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            if len(digits) == 1:
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        digits[-1] += 1
        return digits


digits = [9, 9]
obj = Solution()
print(obj.plusOne(digits))  # [1, 0, 0]


################## *** Вариант 2 *** ##################


class Solution:
    def plusOne(self, digit: list[int]) -> list[int]:
        for i in range(len(digit) - 1, -1, -1):
            if digit[i] == 9:
                digit[i] = 0
            else:
                digit[i] += 1
                return digit

        digit.append(0)
        digit[0] = 1
        return digit


digits = [9, 9]
obj = Solution()
print(obj.plusOne(digits))  # [1, 0, 0]

# ***********************************************************************************************************************
'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a + b)[2:])


a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a, b))  # 100

# ***********************************************************************************************************************
'''
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''
from math import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))


x = 4
obj = Solution()
print(obj.mySqrt(x))  # 2

# ***********************************************************************************************************************
'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Вы поднимаетесь по лестнице. Требуется n шагов, чтобы добраться до вершины. 
Каждый раз вы можете подняться на 1 или 2 ступеньки. Сколькими различными способами вы можете подняться на вершину?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one + two
            one = two
            two = temp
        return two


n = 4
obj = Solution()
print(obj.climbStairs(n))  # 5

# ***********************************************************************************************************************
'''
15) 83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
Учитывая заголовок отсортированного связанного списка, удалите все дубликаты, чтобы каждый элемент появлялся только один раз.
Возвращает также отсортированный связанный список.
  
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

obj = Solution()
result = obj.deleteDuplicates(head)

print()
while result:
    print(result.val)
    result = result.next

# ***********************************************************************************************************************
'''
16) 88. Merge Sorted Array (Объединить отсортированный массив)
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 
Вам даны два массива целых чисел nums1 и nums2, отсортированные в неубывающем порядке, и два целых числа m и n, 
представляющие количество элементов в nums1 и nums2 соответственно.

Объедините nums1 и nums2 в один массив, отсортированный в неубывающем порядке.

Окончательный отсортированный массив не должен возвращаться функцией, а должен храниться внутри массива nums1. 
Чтобы приспособиться к этому, nums1 имеет длину m + n, где первый m элементов обозначают элементы, которые следует объединить,
а последним n элементам присваивается значение 0, и их следует игнорировать. nums2 имеет длину n.
 
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> list:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()
        return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

obj = Solution()
print(obj.merge(nums1, m, nums2, n))

# ***********************************************************************************************************************
'''
17) 100. Same Tree (То же дерево)
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Имея корни двух бинарных деревьев p и q, напишите функцию, проверяющую, совпадают ли они или нет. 
Два бинарных дерева считаются одинаковыми, если они структурно идентичны, а узлы имеют одинаковое значение.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        def compare(pnode, qnode):
            if not pnode and not qnode:
                return True
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False
            return compare(pnode.left, qnode.left) and compare(pnode.right, qnode.right)

        return compare(p, q)


head1 = TreeNode(1)
head1.left = TreeNode(2)
head1.right = TreeNode(3)

head2 = TreeNode(1)
head2.left = TreeNode(2)
head2.right = TreeNode(3)

obj = Solution()
result = obj.isSameTree(head1, head2)

print(result)

# ***********************************************************************************************************************
'''
18) 101. Symmetric Tree (Симметричное дерево)
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Учитывая корень бинарного дерева, проверьте, является ли он зеркалом самого себя (т. Е. Симметричным относительно своего центра).
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


# Создание первого дерева
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

# Создание второго дерева
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

# Создание экземпляра класса Solution
solution = Solution()

print(root1)
# Проверка первого дерева на симметричность
print(solution.isSymmetric(root1))  # Вывод: True

print(root2)
# Проверка второго дерева на симметричность
print(solution.isSymmetric(root2))  # Вывод: False

# ***********************************************************************************************************************
'''
19) 108.Convert Sorted Array to Binary Search Tree (Преобразование отсортированного массива в двоичное дерево поиска)
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Дан целочисленный массив nums, в котором элементы отсортированы в порядке возрастания, преобразовать его в 
сбалансированный по высоте бинарное дерево поиска.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        n = len(nums)
        root = TreeNode()
        stack = [(0, n, root)]

        while stack:
            i, j, node = stack.pop()
            mid = (i + j) // 2
            node.val = nums[mid]

            if mid > i:
                node.left = TreeNode()
                stack.append((i, mid, node.left))
            if mid + 1 < j:
                node.right = TreeNode()
                stack.append((mid + 1, j, node.right))

        return root


# Создаем объект класса Solution
sol = Solution()

# Создаем дерево на основе отсортированного списка
nums = [1, 2, 3, 4, 5, 6, 7]
root = sol.sortedArrayToBST(nums)

# Выводим значения дерева
print(root.val)  # 4
print(root.left.val, root.right.val)  # 2 6
print(root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)  # 1 3 5 7
'''
4
2 6
1 3 5 7
'''
# ***********************************************************************************************************************
'''
20) 110. Balanced Binary Tree (Сбалансированное бинарное дерево)
Given a binary tree, determine if it is height-balanced .
Дано бинарное дерево, определите, является ли оно сбалансированный по высоте.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        return self.Height(root) >= 0

    def Height(self, root):
        if root is None:
            return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1


# Создаем дерево
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Создаем экземпляр класса Solution
s = Solution()

# Вызываем метод isBalanced() и выводим результат
print(s.isBalanced(root))  # Output: True
# ***********************************************************************************************************************
'''
111. Minimum Depth of Binary Tree (Минимальная глубина бинарного дерева.)
iven a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        depth, rightMost = 1, root
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node == rightMost:
                depth += 1
                if node.right is not None:
                    rightMost = node.right
                else:
                    rightMost = node.left
        return depth


# Создаем тестовое дерево
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Создаем экземпляр класса Solution
s = Solution()

# Вызываем функцию minDepth на тестовом дереве
result = s.minDepth(root)

# Выводим результат
print(result)  # 2

# ***********************************************************************************************************************
'''
112. Path Sum (Сумма пути)
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
Учитывая корень двоичного дерева и целое число targetSum, вернуть true, если дерево имеет путь от корня к листу, такой
что суммирование всех значений на пути равно targetSum.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)

solution = Solution()
target_sum = 22

result = solution.hasPathSum(tree, target_sum)
print(result)

# ***********************************************************************************************************************
'''
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
        '''

        ans = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = ans[i - 2][j] + ans[i - 2][j - 1]
            ans.append(row)
        return ans


obj = Solution()
print(obj.generate(4))

# ***********************************************************************************************************************
'''
119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Учитывая целое число rowIndex, вернуть rowIndexth (с индексом 0) строку треугольника Паскаля.
В треугольнике Паскаля каждое число представляет собой сумму двух чисел непосредственно над ним, как показано:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        for i in range(rowIndex + 1):
            res.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[rowIndex]


obj = Solution()
print(obj.getRow(5))  # [1, 5, 10, 10, 5, 1]
# ***********************************************************************************************************************
'''
121. Best Time to Buy and Sell Stock (Лучшее время для покупки и продажи акций)
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

Вам дан массив цен, где цены[i] — цена данной акции на i-й день.
Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции и выбрав другой день в будущем для продажи этой акции.
Верните максимальную прибыль, которую вы можете получить от этой сделки. Если вы не можете получить никакой прибыли, верните 0.
'''


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max = 0
        min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]

            elif (prices[i] - min) > max:
                max = prices[i] - min

        return max


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(obj.maxProfit([7, 6, 4, 3, 1]))  # 0

# ***********************************************************************************************************************
'''
26) 125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Фраза является палиндромом, если после преобразования всех прописных букв в строчные и удаления 
всех неалфавитно-цифровых символов она читается одинаково вперед и назад. Буквенно-цифровые 
символы включают в себя буквы и цифры.
Учитывая строку s, верните true, если это палиндром, или false в противном случае.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower().replace(',', '').replace(':', '').replace('.', '').replace(' ', '')
        s = s.lower()
        res = ''
        for i in s:
            if i.isalpha():
                res += i
            elif i.isnumeric():
                res += i
        return res == res[::-1]


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(obj.isPalindrome("race a car"))  # False
print(obj.isPalindrome("0P"))
# ***********************************************************************************************************************
'''
27) 136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
В непустом массиве целых чисел nums каждый элемент встречается дважды, кроме одного. Найди ту единственную. 
Вы должны реализовать решение с линейной сложностью времени выполнения и использовать только постоянное дополнительное пространство.
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[0] ^= nums[i]
        # return nums[0]

        return 2 * sum(set(nums)) - sum(nums)

        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         del seen[num]
        #     else:
        #         seen[num] = True
        # return list(seen.keys())[0]


obj = Solution()
print(obj.singleNumber([4, 1, 1]))  # 4

# ***********************************************************************************************************************
# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################


'''
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
Вам выдается массив уникальных целых чисел salary, где salary[i] - это зарплата i-го сотрудника.
Верните среднюю заработную плату сотрудников без учета минимальной и максимальной заработной платы.
Будут приняты ответы в пределах 10-5 от фактического ответа.

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


salary = [4000, 3000, 1000, 2000]
obj = Solution()
print(obj.average(salary))  # 2500.0

salary = [4000, 3000, 1000, 2000]
obj = Solution()
print(obj.average(salary))  # 2500.0

# ***********************************************************************************************************************
'''
2678. Number of Senior Citizens (Количество пожилых граждан)
You are given a 0-indexed array of strings details. Each element of details provides information about 
a given passenger compressed into a string of length 15. The system is such that:
Вам дан массив деталей строк с индексом 0. Каждый элемент сведений предоставляет информацию 
о данном пассажире, сжатую в строку длиной 15. Система такова, что:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.

Example 1:
Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. 
Thus, there are 2 people who are over 60 years old.

Example 2:
Input: details = ["1313579440F2036","2921522980M5644"]
Output: 0
Explanation: None of the passengers are older than 60.
'''


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        l = []
        for i in details:
            age = int(i[-4:-2])
            if age > 60:
                l.append(age)
        return len(l)
        # return sum(int(p[-4:-2]) > 60 for p in details)


details = ["9751302862F0693",
           "3888560693F7262",
           "5485983835F0649",
           "2580974299F6042",
           "9976672161M6561",
           "0234451011F8013",
           "4294552179O6482"]
obj = Solution()
print(obj.countSeniors(details))

# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################
