# ***********************************************************************************************************************
''''

(8 kyu)
    1) Even or Odd
    2) Sum of positive
    3) Return Negative
    4) Reversed Strings
    5) Convert boolean values to strings 'Yes' or 'No'.


(7 kyu)
    1) Vowel Count (Количество гласных)
    2) Disemvowel Trolls (Потрошители троллей)
    3) Highest and Lowest
    4) Descending Order (В порядке убывания)
    5) Get the Middle Character (Получить средний персонаж)
    6) Mumbling(бормотание)
    7) You're a square! (Ты квадрат!)
    8) List Filtering (Фильтрация списка)
    9) Isograms (Изограммы)
    10) Exes and Ohs (Бывшие и Оз)
    11) Jaden Casing Strings
    12) Shortest Word (Самое короткое слово)
    13) Complementary DNA (Комплементарная ДНК)
    14) Credit Card Mask (Маска кредитной карты)
    15) Sum of two lowest positive integers (Сумма двух наименьших положительных целых чисел)
    16) Beginner Series #3 Sum of Numbers (Серия для начинающих №3 Сумма чисел)
    17) Two to One
    18) Friend or Foe? (Друг или враг?)
    19) Find the next perfect square! (Найдите следующий идеальный квадрат!)



(6 kyu)
    1) Multiples of 3 or 5 (Кратные 3 или 5)
    2) Stop gninnipS My sdroW! (Остановить гниннипс Мой sdroW!)
    3) Find the odd int (Найдите нечетное целое)
    4) Sum of Digits / Digital Root (Сумма цифр / цифровой корень)
    5) Who likes it?
    6) Array.diff
    7) Bit Counting (Подсчет битов)
    8) Find The Parity Outlier
    9) Counting Duplicates (Подсчет дубликатов)
    10) Duplicate Encoder (Дублирующий кодировщик)
    11) Take a Ten Minutes Walk - 'не сделал'
    12) Replace With Alphabet Position (Заменить позицией в алфавитном порядке)
    13) Persistent Bugger (Настойчивый негодник)
    14) Your order, please
    15) Convert string to camel case - 'не добавил'
    16) Tribonacci Sequence - 'не добавил'
    17) Does my number look big in this? (Мой номер выглядит большим в этом?) - 'не добавил'
    18) Unique In Order (Уникальность в порядке) - 'не добавил'
    19) Find the unique number (Найдите уникальный номер)
    20) Find the missing letter (Найдите недостающую букву)






(5 kyu)
    1) Moving Zeros To The End (Перемещение нулей в конец)
    2) Simple Pig Latin
    3) Human Readable Time (Человекочитаемое время)
    4) RGB To Hex Conversion (Преобразование RGB в шестнадцатеричный формат)
    5) Maximum subarray sum (Максимальная сумма подмассива)
    6) Valid Parentheses (Допустимые скобки)
    7) Directions Reduction (Направления Сокращение)
    8) Calculating with Functions (Расчет с функциями)


'''
# ***********************************************************************************************************************
### *** (8 kyu) *** ###
'''
(8 kyu) 
1) Even or Odd
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
Создайте функцию, которая принимает целое число в качестве аргумента и возвращает "Четное" для четных чисел или "Нечетное" для нечетных чисел.
'''


################## *** Вариант 1 *** ##################
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


print(even_or_odd(10))


################## *** Вариант 2 *** ##################
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


print(even_or_odd(9))

################## *** Вариант 3 *** ##################
even_or_odd = lambda number: "Odd" if number % 2 else "Even"
# ***********************************************************************************************************************
'''
(8 kyu) 
2) You get an array of numbers, return the sum of all of the positives ones.
Вы получаете массив чисел, возвращаете сумму всех положительных чисел.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
'''


################## *** Вариант 1 *** ##################
def positive_sum(arr: list):
    summ = 0
    for i in arr:
        if i > 0:
            summ += i
    return summ


a = [1, -4, 7, 12]
print(positive_sum(a))


################## *** Вариант 2 *** ##################
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# ***********************************************************************************************************************
'''
(8 kyu) 
3) Return Negative
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
В этом простом задании вам дается число, и вы должны сделать его отрицательным. А может быть, число уже отрицательное?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
'''


def make_negative(number):
    # return -number if number > 0 else number
    # return abs(number) * -1
    # return 0 - abs(number)
    return -abs(number)


print(make_negative(-5))  # -5
# ***********************************************************************************************************************
'''
(8 kyu)
4) Reversed Strings
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
'''


def solution(string):
    # return ''.join([str for str in string][::-1])
    # solution = lambda s: s[::-1]
    # return ''.join(i for i in reversed(string))
    # solution=lambda _:_[::-1]
    return string[::-1]


print(solution('world'))  # dlrow

'''
(8 kyu)
 5) Convert boolean values to strings 'Yes' or 'No'.
 Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" 
 string for false.
 
 Завершите метод, который принимает логическое значение и возвращает строку «Да» для значения 
 «истина» или строку «Нет» для значения «ложь» 
'''


def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    return 'No'
    # return "Yes" if boolean else "No"


print(bool_to_word(0))

# ***********************************************************************************************************************


### *** (7 kyu) *** ###

'''
(7 kyu)
1) Vowel Count (Количество гласных)
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

Возвратите количество гласных в заданной строке. 
Мы будем рассматривать a, e, i, o, u как гласные для этой Ката (но не y). 
Входная строка будет состоять только из строчных букв и/или пробелов.
'''


def get_count(sentence):
    return len([i for i in sentence if i in 'aeiouAEIOU'])


print(get_count('hello friend'))

# ***********************************************************************************************************************
'''
(7 kyu)
2) Disemvowel Trolls (Потрошители троллей)
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.

Тролли атакуют ваш раздел комментариев!
Распространенный способ справиться с этой ситуацией - удалить все гласные из комментариев троллей, нейтрализовав угрозу.
Ваша задача состоит в том, чтобы написать функцию, которая принимает строку и возвращает новую строку с удаленными всеми гласными.
Например, строка "Этот сайт для неудачников, ЛОЛ!" превратилась бы в "Это wbst s fr lsrs LL!".
Примечание: в этом ката y не считается гласной.
'''


def disemvowel(string_):
    empty_str = ''
    for i in string_:
        if i not in 'aeiouAEIOU':
            empty_str += i
    return empty_str


a = "This website is for losers LOL!"
print(disemvowel(a))  # Ths wbst s fr lsrs LL!

# ***********************************************************************************************************************
'''
(7 kyu)
3) Highest and Lowest
'''


def high_and_low(numbers):
    l = list(map(int, numbers.split()))
    # l = [int(i) for i in numbers.split()]
    return f'{max(l)} {min(l)}'


s = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'
print(high_and_low(s))

# ***********************************************************************************************************************
'''
(7 kyu)
4) Descending Order (В порядке убывания)
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits 
in descending order. Essentially, rearrange the digits to create the highest possible number.

Ваша задача состоит в том, чтобы создать функцию, которая может принимать любое неотрицательное целое число
в качестве аргумента и возвращать его с цифрами в порядке убывания. По сути, переставьте цифры, 
тобы получить максимально возможное число.
Examples:
Input: 42145        Output: 54421
Input: 145263       Output: 654321
Input: 123456789    Output: 987654321
'''


def descending_order(num: int) -> int:
    s = str(num)
    res = ''
    for i in sorted(list(map(str, s)), reverse=True):
        res += i
    return int(res)


print(descending_order(42145))  # 54421
# ***********************************************************************************************************************
'''
(7 kyu)
5) Get the Middle Character (Получить средний персонаж)
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

Вам дадут слово. Ваша задача — вернуть средний символ слова. Если длина слова нечетная, вернуть средний символ. 
Если длина слова четная, верните средние 2 символа.

Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
'''


################## *** Вариант 1 *** ##################
def get_middle(s):
    if len(s) % 2 == 0:
        return f'{s[int((len(s) / 2) - 1)]}{s[int(len(s) / 2)]}'
    elif len(s) % 2 == 1:
        return s[len(s) // 2]


print(get_middle("testing"))  # t
print(get_middle("test"))  # es
print(get_middle("middle"))  # dd


################## *** Вариант 2 *** ##################
def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s


print(get_middle("testing"))  # t
print(get_middle("test"))  # es
print(get_middle("middle"))  # dd


################## *** Вариант 3 *** ##################
def get_middle(s):
    return s if len(s) <= 2 else get_middle(s[1:-1])


print(get_middle("testing"))  # t
print(get_middle("test"))  # es
print(get_middle("middle"))  # dd


################## *** Вариант 4 *** #################
def get_middle(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    return s[len(s) // 2 - 1: len(s) // 2 + 1]


print(get_middle('test'))  # es
print(get_middle('middle'))  # dd
print(get_middle('testing'))  # t

# ***********************************************************************************************************************
'''
(7 kyu)
6) Mumbling(бормотание)
This time no story, no theory. The examples below show you how to write function accum:
The parameter of accum is a string which includes only letters from a..z and A..Z.

На этот раз ни истории, ни теории. В приведенных ниже примерах показано, как написать функцию accum:
Параметр accum представляет собой строку, включающую только буквы из a..z и A..Z.

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

'''


def accum(s: str) -> str:
    res = ''
    for i, count in enumerate(s):
        res += count.upper() + count.lower() * i + '-'
    return res[:-1]


print(accum('cwAt'))
print(accum("abcd"))

# ***********************************************************************************************************************

'''
(7 kyu)
7) You're a square! (Ты квадрат!)
A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!
However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.
Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
'''
from math import sqrt


def is_square(n):
    # return n >= 0 and (n ** 0.5) % 1 == 0 # тоже все верно
    # return n>=0 and sqrt(n).is_integer() # тоже все верно
    if n >= 0 and n == sqrt(n) ** 2:
        return True
    elif n == 3:
        return False
    else:
        return False


print(is_square(16))  # True
print(is_square(4))  # True
print(is_square(25))  # True
print(is_square(26))  # False
'''
(7 kyu)
8) List Filtering (Фильтрация списка)
In this kata you will create a function that takes a list of non-negative integers and
strings and returns a new list with the strings filtered out.
'''


def filter_list(l):
    return [i for i in l if i != str(i)]


# ***********************************************************************************************************************
'''
(7 kyu)
9) Isograms (Изограммы)

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case
  
Изограмма — это слово, в котором нет повторяющихся букв, последовательных или непоследовательных. 
Реализуйте функцию, определяющую, является ли строка, содержащая только буквы, изограммой. 
Предположим, что пустая строка является изограммой. Игнорировать регистр букв
'''


def is_isogram(string):
    string = string.lower()
    if len(string) == len(set(string)):
        return True
    return False


s1 = 'Dermatoglyphics'
s2 = 'moose'
print(is_isogram(s1))  # True
print(is_isogram(s2))  # False

'''
(7 kyu)
10) Exes and Ohs (Бывшие и Оз)

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
The string can contain any char.
Проверьте, содержит ли строка одинаковое количество «x» и «o». Метод должен возвращать логическое значение и не 
учитывать регистр. Строка может содержать любой символ.

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''


def xo(s):
    s = s.lower()
    if s.count('x') == s.count('o'):
        return True
    return False


print(funk("ooxXm"))  # True

# ***********************************************************************************************************************
'''
(7 kyu)
11) Jaden Casing Strings
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''


def to_jaden_case(string):
    l = string.split()
    res = [i.capitalize() for i in l]
    return ' '.join(res)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# ***********************************************************************************************************************
'''
(7 kyu)
12) Shortest Word (Самое короткое слово)
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

Просто, учитывая строку слов, вернуть длину кратчайшего слова (слов). 
Строка никогда не будет пустой, и вам не нужно учитывать разные типы данных.
'''


def find_short(s):
    # return min([len(i) for i in s.split()]) можно так
    res = []
    for i in s.split():
        res.append(len(i))
    return min(res)


s1 = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s1))

# ***********************************************************************************************************************
'''
(7 kyu)
13) Complementary DNA (Комплементарная ДНК)
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the 
development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of 
the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or
there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''


# вариант 1
def DNA_strand(s):
    res = ''
    for i in s:
        if i == 'A':
            res += 'T'
        elif i == 'T':
            res += 'A'
        elif i == 'G':
            res += 'C'
        else:
            res += 'G'
    return res


# вариант 2
def DNA_strand(dna):
    d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    res = ''
    for i in dna:
        res += d[i]
    return res


print(DNA_strand("GTAT"))  # CATA
print(DNA_strand("AAAA"))  # TTTT
print(DNA_strand("GTAT"))  # CATA
# ***********************************************************************************************************************
'''
(7 kyu)
14) Credit Card Mask (Маска кредитной карты)

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
'''


def maskify(cc):
    return (len(cc) - 4) * '#' + cc[-4:]


print(maskify("4556364607935616"))
# ***********************************************************************************************************************
'''
(7 kyu)
15) Sum of two lowest positive integers (Сумма двух наименьших положительных целых чисел)
    
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
 No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''


def sum_two_smallest_numbers(numbers):
    # your code here
    numbers.sort()
    return numbers[0] + numbers[1]


print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
# ***********************************************************************************************************************
'''
(7 kyu)
16) Beginner Series #3 Sum of Numbers (Серия для начинающих №3 Сумма чисел)

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and
including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)'''


def get_sum(a, b):
    # можно так
    if a == b:
        return a
    elif a > b:
        return sum([i for i in range(b, a + 1)])
    elif a < b:
        return sum([i for i in range(a, b + 1)])

    # а можно так
    # return a if a == b else sum([i for i in range(b, a + 1)] if a > b else [i for i in range(a, b + 1)])


print(get_sum(1, 0))  # 1
# ***********************************************************************************************************************
'''
(7 kyu)
17) Two to One

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''


################## *** Вариант 1 *** ##################
def longest(a1, a2):
    set3 = set(a1).union(a2)
    return ''.join(sorted(set3))


################## *** Вариант 2 *** ##################
def longest(a1, a2):
    return ''.join(sorted(set([i for i in (a1 + a2)])))


# ***********************************************************************************************************************
'''
   (7 kyu)
   
18) Friend or Foe? (Друг или враг?)
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, 
you can be sure he's not...

Создайте программу, которая фильтрует список строк и возвращает список, содержащий только имена ваших друзей. 
Если в имени ровно 4 буквы, можете быть уверены, что оно должно быть вашим другом! В противном случае, вы можете 
быть уверены, что он не...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
'''


def friend(x):
    return [x for x in x if len(x) == 4]


print(friend(["Ryan", "Kieran", "Jason", "Yous"]))  # ["Ryan", "Yous"]

# ***********************************************************************************************************************

'''    
19) Find the next perfect square! (Найдите следующий идеальный квадрат!)

You might know some pretty large perfect squares. But what about the NEXT one?
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative

Возможно, вы знаете несколько довольно больших идеальных квадратов. Но как насчет следующего?
Завершите метод find Next Square, который находит следующий интегральный идеальный квадрат после того, который был передан
в качестве параметра.
Напомним, что целым идеальным квадратом является целое число n, такое, что sqrt(n) также является целым числом.
Если параметр сам по себе не является идеальным квадратом, то должно быть возвращено значение -1. Вы можете предположить, 
что параметр неотрицателен

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
'''


def find_next_square(sq):
    if sq ** 0.5 == int(sq ** 0.5):
        return int(((sq ** 0.5) + 1) ** 2)
    return -1


print(find_next_square(625))  # 676

# ***********************************************************************************************************************


# ***********************************************************************************************************************


# ***********************************************************************************************************************

# ***********************************************************************************************************************


# ***********************************************************************************************************************


# ***********************************************************************************************************************
### *** (6 kyu) *** ###
# ***********************************************************************************************************************

# ***********************************************************************************************************************
'''
(6 kyu) 
1) Multiples of 3 or 5 (Кратные 3 или 5)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Finish the solution so that it returns the sum of all the multiples 
of 3 or 5 below the number passed in. Additionally, if the number is negative, return 
0 (for languages that do have them). Note: If the number is a multiple of both 3 and 5, 
only count it once.

Если мы перечислим все натуральные числа ниже 10, кратные 3 или 5, мы получим 3, 5, 6 и 9.
Сумма этих кратных равна 23. Завершите решение так, чтобы оно возвращало сумму всех значений, 
кратных 3 или 5, ниже переданного числа. Кроме того, если число отрицательное, верните 
0 (для языков, в которых они есть). Примечание: Если число кратно как 3, так и 5, 
подсчитайте его только один раз.
'''


################## *** Вариант 1 *** ##################
def solution(n):
    l = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    return sum(l)


print(solution(10))


################## *** Вариант 2 *** ##################
def solution(number: int) -> int:
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


print(solution(10))

################## *** Вариант 3 *** ##################
solution = lambda n: sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(solution(10))

# ***********************************************************************************************************************
'''
(6 kyu)

2) Stop gninnipS My sdroW! (Остановить гниннипс Мой sdroW!)

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more 
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Напишите функцию, которая принимает строку из одного или нескольких слов и возвращает ту же строку, но со всеми пятью 
или более буквенными словами наоборот (точно так же, как название этого Ката). Передаваемые строки будут состоять 
только из букв и пробелов. Пробелы будут включены только в том случае, если присутствует более одного слова.

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''


def spin_words(sentence: str) -> str:
    l = []
    for i in [i for i in sentence.split()]:
        if len(i) >= 5:
            i = i[::-1]
        l.append(i)
    return ' '.join(l)


print(spin_words("Hey fellow warriors"))  # Hey wollef sroirraw
# ***********************************************************************************************************************
'''
(6 kyu)

3) Find the odd int (Найдите нечетное целое)

Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Дан массив целых чисел, найдите то, которое встречается нечетное количество раз. 
Всегда будет только одно целое число, которое встречается нечетное количество раз.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

'''


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i


# ***********************************************************************************************************************
'''
(6 kyu)

4) Sum of Digits / Digital Root (Сумма цифр / цифровой корень)

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until 
a single-digit number is produced. The input will be a non-negative integer.

Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной цифры, продолжайте уменьшать таким образом, 
пока не будет получено однозначное число. Ввод будет неотрицательным целым числом.

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''


################## *** Вариант 1 *** ##################

def digital_root(number):
    l = [int(i) for i in str(number)]
    if sum(l) > 9:
        return digital_root(sum(l))
    return sum(l)


print(digital_root(16))  # 7
print(digital_root(942))  # 6
print(digital_root(132189))  # 6
print(digital_root(493193))  # 2


################## *** Вариант 2 *** ##################
def digital_root(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n //= 10
    if sum(l) > 9:
        return digital_root(sum(l))
    return sum(l)


print(digital_root(493193))  # 2

# ***********************************************************************************************************************
'''
(6 kyu)

5) Who likes it?
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names[2:])} others like this'


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))

'''
(6 kyu)

6) Array.diff
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

Ваша цель в этом ката — реализовать функцию разности, которая вычитает один список из другого и возвращает результат. 
Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.

array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]
'''


def array_diff(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res
    # return [i for i in a if i not in b]


print(array_diff([1, 2], [1]))  # [2]
print(array_diff([1, 2, 2], [1]))  # [2, 2]
# ***********************************************************************************************************************


'''
(6 kyu)

7) Bit Counting (Подсчет битов)

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary 
representation of that number. You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

Напишите функцию, которая принимает целое число в качестве входных данных и возвращает количество битов, равных единице
в двоичном представлении этого числа. Вы можете гарантировать, что входные данные неотрицательны.
Пример: Двоичное представление 1234 равно 10011010010, поэтому в этом случае функция должна возвращать 5
'''


################## *** Вариант 1 *** ##################
def count_bits(n):
    return str(bin(n)[2:]).count('1')


################## *** Вариант 2 *** #################
def count_bits(n):
    return [i for i in bin(n)[2:]].count('1')


################## *** Вариант 3 *** #################
def count_bits(n):
    return bin(n).count('1')


print(funk(1234))  # 5

#
# ***********************************************************************************************************************
'''
(6 kyu)

8) Find The Parity Outlier
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array 
is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Вам предоставляется массив (который будет иметь длину не менее 3, но может быть очень большим), содержащий целые числа. 
Массив либо полностью состоит из нечетных целых чисел, либо полностью состоит из четных целых чисел, за исключением 
единственного целого числа N. Напишите метод, который принимает массив в качестве аргумента и возвращает этот "выброс" N.

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''


def find_out(integers: list) -> int:
    l1 = [i for i in integers if i % 2 == 0]
    l2 = [i for i in integers if i % 2 == 1]
    if len(l1) < len(l2):
        return l1[0]
    return l2[0]


print(find_out([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11
print(find_out([160, 3, 1719, 19, 11, 13, -21]))  # 160

# ***********************************************************************************************************************
'''
(6 kyu)

9) Counting Duplicates (Подсчет дубликатов)
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase
and lowercase) and numeric digits.

Напишите функцию, которая будет возвращать количество различных нечувствительных к регистру буквенных символов и цифровых 
цифр, которые встречаются во входной строке более одного раза. Можно предположить, что входная строка содержит только
буквы (как прописные, так и строчные) и числовые цифры.

'''


def duplicate_count(text):
    text = text.lower()
    d = {i: text.count(i) for i in text}
    l = [i for i in d if d[i] >= 2]
    return len(l)


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
# ***********************************************************************************************************************
'''
(6 kyu)

10) Duplicate Encoder (Дублирующий кодировщик)
 The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in the 
original string. Ignore capitalization when determining if a character is a duplicate.

Цель этого упражнения - преобразовать строку в новую строку, где каждый символ в новой строке равен "("
, если этот символ появляется только один раз в исходной строке, или ")", если этот символ появляется более одного раза в
исходной строке. Игнорируйте заглавные буквы при определении того, является ли символ дубликатом.
'''


def duplicate_encode(word):
    res = ''
    word = word.lower()
    for i in word:
        if word.count(i) == 1:
            res += '('
        else:
            res += ')'
    return res


print(duplicate_encode("din"))  # (((
print(duplicate_encode("recede"))  # ()()()
print(duplicate_encode("Success"))  # )())())
print(duplicate_encode("(( @"))  # ))((

# ***********************************************************************************************************************
'''
(6 kyu)

12) Replace With Alphabet Position (Заменить позицией в алфавитном порядке)

In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

В этой ката вы должны, учитывая строку, заменить каждую букву ее позицией в алфавите. 
Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.

"a" = 1, "b" = 2, etc.
'''

import string


def alphabet_position(text):
    d = {key: str(i) for i, key in enumerate(string.ascii_lowercase, 1)}
    res = ''
    for i in text.lower():
        if i.isalpha():
            res += d[i] + ' '
    return res[:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))
# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11

# ***********************************************************************************************************************
'''
(6 kyu)

13) Persistent Bugger (Настойчивый негодник)
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
Напишите функцию persistence, которая принимает положительный параметр num и возвращает его мультипликативную стойкость,
то есть количество раз, которое вы должны умножить на num, пока не получите одну цифру. 

Например 
For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''


def persistence(n):
    if n < 10:
        return 0
    proiz = 1
    for i in str(n):
        proiz *= int(i)
    return 1 + persistence(proiz)


print(persistence(39))  # 3
print(persistence(999))  # 4
print(persistence(4))  # 0

# ***********************************************************************************************************************
'''(6 kyu)

14) Your order, please
Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid 
consecutive numbers.

Ваша задача — отсортировать заданную строку. Каждое слово в строке будет содержать одно число. Это число — позиция,
которую слово должно занимать в результате.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''


def order(sentence):
    l = []
    for i in range(len(sentence) + 1):
        for j in sentence.split():
            if str(i) in j:
                l.append(j)
    return ' '.join(l)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))

# ***********************************************************************************************************************
'''
(6 kyu)

19) There is an array with some numbers. All numbers are equal except for one. Try to find it!
Есть массив с некоторыми числами. Все числа равны, кроме одного. Попробуйте найти!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
'''


def find_uniq(arr):
    l = []
    for i in set(arr):
        if arr.count(i) == 1:
            l.append(i)
    return l[0]
    # return [i for i in set(arr) if arr.count(i) == 1][0]


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))
# ***********************************************************************************************************************


'''
20) Find the missing letter (Найдите недостающую букву)
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)
Have fun coding it and please don't forget to vote and rank this kata! :-)
I have also created other katas. Take a look if you enjoyed this kata!
'''


def find_missing_letter(arr):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    one_elem_arr = abc.find(arr[0])
    l = abc[one_elem_arr: one_elem_arr + len(arr) + 1]
    res = [i for i in l if i not in arr]
    return res[0]


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # e
print(find_missing_letter(['O', 'Q', 'R', 'S']))  # p

### *** (5 kyu) *** ###
# ***********************************************************************************************************************
'''
(5 kyu)

1) Moving Zeros To The End (Перемещение нулей в конец)
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
Напишите алгоритм, который берет массив и перемещает все нули в конец, сохраняя порядок остальных элементов.
'''


def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
print(move_zeros([1, 2, 1, 1, 3, 1, 0, 0, 0, 0]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]

# ***********************************************************************************************************************
'''(5 kyu)

2) Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Переместите первую букву каждого слова в конец, а затем добавьте «ay» в конец слова. Оставьте знаки препинания нетронутыми.

Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


################## *** Вариант 1 *** ##################
def pig_it(text):
    return ' '.join([i[1:] + i[:1] + 'ay' if i.isalpha() else i for i in text.split()])


################## *** Вариант 2 *** ##################
def pig_it(text):
    l = []
    for i in text.split():
        if i.isalpha():
            l.append(i[1:] + i[:1] + 'ay')
        else:
            l.append(i)
    return ' '.join(l)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
# ***********************************************************************************************************************
'''
(5 kyu)
3) Human Readable Time (Человекочитаемое время)

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.

Напишите функцию, которая принимает неотрицательное целое число (секунды) в качестве входных данных и возвращает время в удобочитаемом формате (ЧЧ:ММ:СС)
HH = часы, дополненные 2 цифрами, диапазон: 00 - 99
ММ = минуты, дополненные 2 цифрами, диапазон: 00 - 59
SS = секунды, дополненные 2 цифрами, диапазон: 00 - 59
Максимальное время никогда не превышает 359999 (99:59:59)
Вы можете найти несколько примеров в тестовых приложениях.
'''


################## *** Вариант 1 *** ##################
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


print(make_readable(0))  # 00:00:00
print(make_readable(5))  # 00:00:05
print(make_readable(60))  # 00:01:00
print(make_readable(86399))  # 23:59:59
print(make_readable(359999))  # 99:59:59


################## *** Вариант 2 *** ##################
def make_readable(n):
    return f'{n // 3600:02d}:{(n % 3600) // 60:02d}:{n % 60:02d}'


################## *** Вариант 3 *** ##################
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"


print(make_readable(200))  # 00:03:20

# ***********************************************************************************************************************
'''
(5 kyu)
4) RGB To Hex Conversion (Преобразование RGB в шестнадцатеричный формат)
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range 
must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Функция rgb является неполной. Завершите его так, чтобы передача десятичных значений RGB привела к возвращению
шестнадцатеричного представления. Допустимыми десятичными значениями для RGB являются 0 - 255. Любые значения, 
выходящие за пределы этого диапазона, должны быть округлены до ближайшего допустимого значения.

Примечание: Ваш ответ всегда должен содержать 6 символов, сокращение с 3 здесь не сработает.


The following are examples of expected output values:
Ниже приведены примеры ожидаемых выходных значений:
'''


def funk(num):
    if num <= 0:
        return '00'
    if num >= 255:
        return 'FF'
    if len(hex(num)[2:]) == 2:
        return hex(num)[2:].upper()
    else:
        return '0' + hex(num)[2:].upper()


def rgb(r, g, b):
    return funk(r) + funk(g) + funk(b)


print(rgb(0, 0, 0))  # 000000
print(rgb(255, 255, 255))  # FFFFFF
print(rgb(255, 255, 300))  # FFFFFF
print(rgb(148, 0, 211))  # 9400D3
print(rgb(0, 1, 2))  # 000102
# ***********************************************************************************************************************
'''
(5 kyu)
5) Maximum subarray sum (Максимальная сумма подмассива)

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

Задача подмассива с максимальной суммой состоит в нахождении максимальной суммы непрерывной подпоследовательности в массиве или списке целых чисел:
max_sequence максимальная последовательность([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# должно быть 6: [4, -1, 2, 1]
Простой случай - это когда список состоит только из положительных чисел, а максимальная сумма равна сумме всего массива. Если список состоит только из отрицательных чисел, верните вместо них 0.
Считается, что пустой список имеет нулевую наибольшую сумму. Обратите внимание, что пустой список или массив также является допустимым подсписком/подмассивом.
'''


def max_sequence(arr):
    max = 0
    cur = 0
    for i in arr:
        cur += i
        if cur < 0:
            cur = 0
        if cur > max:
            max = cur
    return max


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))  # 0
# ***********************************************************************************************************************

'''
(5 kyu)
6) Valid Parentheses (Допустимые скобки)
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Напишите функцию, которая принимает строку скобок и определяет, допустим ли порядок скобок. 
Функция должна возвращать true, если строка допустима, и false, если она недействительна.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''


################## *** Вариант 1 *** ##################
def valid_parentheses(string):
    res = []
    for i in string:
        if i == '(':
            res.append(i)
        elif i == ')':
            try:
                res.pop()
            except:
                return False

    if len(res) == 0:
        return True
    return False


################## *** Вариант 2 *** ##################
def valid_parentheses(string):
    cnt = 0
    for i in string:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


print(valid_parentheses("()"))  # True
print(valid_parentheses("()()()"))  # True
print(valid_parentheses("(()())()"))  # True
print(valid_parentheses("()(())((()))(())()"))  # True
print(valid_parentheses("())(()"))  # False
print(valid_parentheses(")("))  # False
# ***********************************************************************************************************************
'''
(5 kyu)
7) Directions Reduction (Направления Сокращение)
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. 
Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, 
otherwise you might die of thirst!

...мужчине дали указания, как добраться из одной точки в другую. Направления были "СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК".
Очевидно, что "СЕВЕР" и "ЮГ" противоположны, "ЗАПАД" и "ВОСТОК" тоже.

Идти в одном направлении и сразу же возвращаться в противоположном - ненужное усилие.
Поскольку это дикий Запад, с ужасной погодой и небольшим количеством воды, важно поберечь немного энергии,
иначе вы можете умереть от жажды!

NORTH	СЕВЕР
SOUTH	ЮГ
	
WEST	запад
EAST	восток
'''


def dirReduc(arr):
    d = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    for i in range(len(arr) - 1):
        if d[arr[i]] == arr[i + 1]:
            del arr[i: i + 2]
            return dirReduc(arr)
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  # ['WEST']

# ***********************************************************************************************************************

'''
(5 kyu)
8) Calculating with Functions (Расчет с функциями)
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
На этот раз мы хотим написать вычисления с использованием функций и получить результаты. Давайте посмотрим на некоторые примеры:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
'''
def zero(param=None): return 0 if param is None else int(param(0))
def one(param=None): return 1 if param is None else int(param(1))
def two(param=None): return 2 if param is None else int(param(2))
def three(param=None): return 3 if param is None else int(param(3))
def four(param=None): return 4 if param is None else int(param(4))
def five(param=None): return 5 if param is None else int(param(5))
def six(param=None): return 6 if param is None else int(param(6))
def seven(param=None): return 7 if param is None else int(param(7))
def eight(param=None): return 8 if param is None else int(param(8))
def nine(param=None): return 9 if param is None else int(param(9))


def plus(i): return lambda x: x+i
def minus(i): return lambda x: x-i
def times(i): return lambda x: x*i
def divided_by(i): return lambda x: x//i


print(seven(times(five())))  # 35
print(four(plus(three())))  # 7
print(eight(minus(three())))  # 5

# ***********************************************************************************************************************
# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################
