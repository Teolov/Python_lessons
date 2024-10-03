# подключаем функцию randint из библиотеки random
from random import randint
# randint(min, max) - генерирует случайное число от min до max
print(randint(2,10))


# создание списка
# arr = [1 , 5, 9 , "hi" , True , 2.8]
# print(arr)
# print(arr[3])


# создание пустого списка
# arr = []
# print(arr)
# append(x) - добавляет элемент x в конец списка 
# arr.append("rtt")
# print(arr)
# arr = [1 , 5, 2.8 , 9 , "hi" , True , 2.8]
# append(x) - удаляет первый попавшийся элемент x
# arr.remove(2.8)
# print(arr)



arr = [1 , 5, 2.8 , 9 , "hi" , True , 2.8]
# перебор списка с помощью цикла for
for i in arr:
    print(i)



# список в списке
arr = [1, [8,9,6] , 5]
print(arr[1][2])




# len(arr) - возвращает длину списка





