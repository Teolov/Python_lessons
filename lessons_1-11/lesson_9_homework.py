# дз
# номер 1
# Напишите функцию для вычисления факториала числа

# def factorial(n): 
#     if n == 0 or n == 1: 
#         return 1
#     else: 
#         return factorial(n-1) * n 

# print(factorial(5))

# номер 2
# Напишите программу для возведения числа n в степень m. 
# нельзя использовать степень (**)

# def step(n, m):
#     if m == 0:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return n * step(n, m -1)
    
# print(step(2,4))

# номер 3
# напишите функцию которая принимает список и возвращает сумму всех чисел списка

from random import *

# def sps(spisok = None):
#     if spisok is None:
#         spisok = [randint(1,10) for i in range(5)]
#     print(spisok)
#     return sum(spisok)

# print(sps([1,2,3,4,5]))

# номер 4
# напишите функцию которая принимает два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
# функция возвращает словарь

# def sps_2(s_1 = None, s_2 = None):
#     if s_1 is None or s_2 is None:
#         s_1 = [randint(1,1000) for i in range(5)]
#         s_2 = [randint(1,1000) for i in range(5)]
#     print(f'{s_1}\n{s_2}')

#     slvr = {}
#     for i in range(len(s_1)):
#         slvr[s_1[i]] = s_2[i]

#     return(slvr)

# print(sps_2())

# номер 5
# Напишите функцию которая принимает список чисел и строк и возвращает список с удалёнными строками

# def func(spisok = None):
#     if not spisok:
#         return []
#     elif isinstance(spisok[0], str) :
#         return func(spisok[1:])
#     else:
#         return [spisok[0]] + func(spisok[1:])

# spisok = [ 1, 2, 3, 'b', 'a', 'j']
# print(func(spisok))


# номер 6
# написать функцию которая принимает строку и изменять её вставляя после каждого символа строки "^"
# пример: 
    # функция принимает "123456" 
    # функция возвращает "1^2^3^4^5^6"

# def func(stroka = '123'):
#     for i in stroka:
#         print(i + '^', end= '')
    
# func('123456')

# def func(stroka = '', index = 0):
#     if index < len(stroka):
#         print(stroka[index] + '^', end= '')
#         return func(stroka, index + 1)
#     else:
#         return ''

# print(func('123456'))

# номер 7
# написать функцию которая принимает строку и число ,
#  функцию возвращает строку умноженную на число нельзя использовать умножение

# def func(stroka = '', num = 0):
#     if num > 0:
#         print (stroka, end='')
#         return func(stroka, num -1)
#     else: 
#         return ''

# func('abc', 5)