# номер 1
# Составить расписание на неделю. 
# Пользователь вводит порядковый номер дня недели и у него на экране отображается, то,
# что запланировано на этот день.

# day = int(input('Введите номер дня недели: '))
# match (day):
#     case 1:
#         print ('Это понедельник :)')
#     case 2:
#         print ('Это вторник :)')
#     case 3:
#         print ('Это среда :)')
#     case 4:
#         print ('Это четверг :)')
#     case 5:
#         print ('Это пятница :)')
#     case 6:
#         print ('Это суббота :)')
#     case 7:
#         print ('Это воскресенье :)')
#     case _:
#         print ('Такого дня не бывает :(')

# номер 2
# сделать программу калькулятор пользователь вводит:
# 1. первое число 
# 2. арифметический оператор
# 3. второе число 

f_num = int(input('First num: '))
opr = input('Operator: ')
s_num = int(input('Second num: '))

match (opr):
    case '*':
        print (f_num * s_num)
    case '/':
        print (f_num / s_num)
    case '-':
        print (f_num - s_num)
    case '+':
        print (f_num + s_num)
    case _:
        print ('Operator does not exist')