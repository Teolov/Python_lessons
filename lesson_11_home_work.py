# задачи на лямбду (lambda):
# номер 1
# дан список чисел все числа которые равны 1, 2, 3 должны стать числом 0 

# arr_1 = [1,2,3,4,5,6,7]
# arr_1_upd = list(map(lambda x: x*0 if (x==1 or x==2 or x==3) else x, arr_1))
# print(arr_1_upd)

# номер 2
# дан список чисел и строк убрать все строки из списка

# arr_2 = [1,2,3,'a', 'b', 'c']
# arr_2_upd = list(map(lambda x: x,  filter(lambda y: isinstance(y,int), arr_2)))
# print(arr_2_upd)

# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой
# пример: 
#     даны списки
#         ar1 = [1,3,6]
#         ar2 = [3,9,2]
#         ответ : [3,9,6]

# ar1 = [1,3,6]
# ar2 = [3,9,6]
# ar3 = list(map(lambda x,y: x if (x > y) else y, ar1,ar2))
# print(ar3)

# номер 4
# дан список в котором списки с числами ,каждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)

arr_3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
def func(ind_1 = 0, ind_2 = 0, num = 2):
    arr_3_1 = []
    arr_3_1.append(arr_3[ind_1][ind_2] * num)
    print(arr_3_1)
    return func(ind_2 + 1)
        

print(func())
------ не успел решить 

