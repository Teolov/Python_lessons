# дз
# номер 1
# сделать программу , которая принимает текст и сохраняет в файл 

# new_text = input('Добавьте новый текст: ')

# open_txt = open('hw_14_1.txt', 'a')
# open_txt.write(f'\n{new_text}')
# open_txt.close()

# open_txt = open('hw_14_1.txt', 'r').read()
# print(open_txt)

# номер 2
# сделать программу калькулятор с историей программа должна показывать историю

f_num = int(input('First num: '))
opr = input('Operator: ')
s_num = int(input('Second num: '))
result = 0

match (opr):
    case '*':
        result = (f_num * s_num)
    case '/':
        result =  (f_num / s_num)
    case '-':
        result =  (f_num - s_num)
    case '+':
        result =  (f_num + s_num)
    case _:
        result =  ('Operator does not exist')

open_txt = open('hw_14_2.txt', 'a')
open_txt.write(f'\n{f_num, opr, s_num} = {result}')
open_txt.close()

open_txt = open('hw_14_2.txt', 'r').read()
print(open_txt)

