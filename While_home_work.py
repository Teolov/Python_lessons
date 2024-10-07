
# # Исправь ошибку !!!

# arr_list = [1,2,4,5 ,7 , 4 ,1]
# index = len(arr_list) 
# while index != 0:
#     print(arr_list[-1])
#     index -= 1
#     arr_list.pop(-1)

# # Задание 1.
# # Вывести на экран все числа от нуля до введенного пользователем числа. 

# num = int(input('vvedite chislo: '))
# i = -1
# while i != num:
#     i += 1
#     print(i)

    
# Задание 2. Пользователь вводит две границы диапазона, 
# вывести на экран все числа из этого диапазона. Предусмотреть, 
# чтобы пользователь мог вводить границы диапазона в произвольном порядке.
# ■ вывести все четные числа из диапазона.
# ■ вывести все нечетные числа из диапазона.
# ■ вывести все числа, кратные семи.

num1 = int(input('vvedite chislo 1: '))
num2 = int(input('vvedite chislo 2: '))
my_list = []
if num1 == num2:
    print('Числа равны: ')
while num1 != num2:
    if num1 < num2:
        my_list.append(num1)
        print(num1)
        num1 += 1
    elif num1 > num2:
        print(num1)
        num1 -= 1
else:
    print(num2)
    my_list.append(num2)

print('Четные числа: ', end = ' ')
for i in my_list:
    if i % 2 == 0:
        print(i, end = ' ')
print()
print('Нечетные числа: ', end = ' ')
for i in my_list:
    if i % 2 != 0:
        print(i, end = ' ')
print()
print('Кратные семи: ', end = ' ')
for i in my_list:
    if i % 7 == 0:
        print(i, end = ' ')
print()
print(my_list)
print(my_list[1::2])
print(my_list[::2])
