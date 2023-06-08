# ***********************************************************************************************************************
''''

(8 kyu)
    1) Even or Odd
    2) Sum of positive
    3) Return Negative
    4) Reversed Strings

(7 kyu)
    1) Vowel Count (Количество гласных)
    2) Disemvowel Trolls (Потрошители троллей)
    3) Highest and Lowest
    4) Descending Order (В порядке убывания)
    5) Get the Middle Character (Получить средний персонаж)
    6) Mumbling(бормотание)
    7) You're a square! (Ты квадрат!)
    8) List Filtering (Фильтрация списка)

(6 kyu)
    1) Sum of Digits / Digital Root (Сумма цифр / цифровой корень)
    2) Multiples of 3 or 5 (Кратные 3 или 5)
(5 kyu)
    1) Human Readable Time (Человекочитаемое время)
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
    b = list(map(int, numbers.split()))
    return f'{max(b)} {min(b)}'


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


def accum(s):
    # your codedef accum(s):
    s = s.lower()  # Приводим строку к нижнему регистру
    result = []  # Список для хранения промежуточных значений
    count = 1  # Счетчик для определения количества повторений символа

    for char in s:
        repeated_char = char * count  # Повторяем символ в соответствии с текущим счетчиком
        capitalized_char = repeated_char.capitalize()  # Первую букву делаем заглавной
        result.append(capitalized_char)  # Добавляем полученное значение в список
        count += 1  # Увеличиваем счетчик

    return '-'.join(result)  # Возвращаем объединенную строку с использованием дефисов


# ***********************************************************************************************************************
print(accum("abcd"))
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
    if n == 0:
        return True
    elif n > 0:
        if n == sqrt(n) ** 2:
            return True
        return False
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
### *** (6 kyu) *** ###
# ***********************************************************************************************************************
'''
(6 kyu) 
1) Sum of Digits / Digital Root (Сумма цифр / цифровой корень)

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
    2) Multiples of 3 or 5 (Кратные 3 или 5)

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
def solution(number: int) -> int:
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


print(solution(10))

################## *** Вариант 2 *** ##################
solution = lambda n: sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
print(solution(10))

### *** (5 kyu) *** ###
# ***********************************************************************************************************************
'''
(5 kyu)
1) Human Readable Time (Человекочитаемое время)

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
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"


print(make_readable(200))  # 00:03:20


################## *** Вариант 2 *** ##################
def make_readable(n):
    return f'{n // 3600:02d}:{(n % 3600) // 60:02d}:{n % 60:02d}'

# ***********************************************************************************************************************
# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################
