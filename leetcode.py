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
100) 101. Symmetric Tree (Симметричное дерево)
101) 1491. Average Salary Excluding the Minimum and Maximum Salary(Средняя заработная плата без учета минимальной и максимальной зп)
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
# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################
