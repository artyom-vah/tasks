# ***********************************************************************************************************************
'''
разворот_строки



'''

# разворот_строки

################## *** Вариант 1 *** ##################
a = 'Hello'
print(a[::-1])  # olleH

################## *** Вариант 1 *** ##################
a = 'hello'
print(''.join(reversed(a)))  # olleH

################## *** Вариант 3 *** ##################
str1 = "pythonist"
res = ''
for i in str1:
    res = i + res
print(res)  # tsinohtyp

# ***********************************************************************************************************************