# ***********************************************************************************************************************
''''
всего 7

(8 kyu)
    1) Even or Odd
    2) Sum of positive
    3) Return Negative
    4) Reversed Strings

(7 kyu)
    1) Vowel Count (Количество гласных)

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
