# ***********************************************************************************************************************
''''
(8 kyu)
(7 kyu)
(6 kyu)
    1) Sum of Digits / Digital Root (Сумма цифр / цифровой корень)
    2) Multiples of 3 or 5 (Кратные 3 или 5)
(5 kyu)

'''

### *** (8 kyu) *** ###
'''
(8 kyu) 
'''

### *** (7 kyu) *** ###
'''
(7 kyu) 
'''

### *** (6 kyu) *** ###
'''
(6 kyu) 
Sum of Digits / Digital Root (Сумма цифр / цифровой корень)

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
Multiples of 3 or 5

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

# ***********************************************************************************************************************
# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
################## *** Вариант 2 *** ##################
