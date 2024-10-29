# номер 1
# создайте класс с тремя переменными 
# у класса есть метод который возвращает все переменные в списке

# class Triple():
#     def __init__(self):
#         self.one = 1
#         self.two = 2
#         self.three = 3
#         self.spisok = []
#     def comeback(self):
#         self.spisok = [self.one, self.two, self.three]
        
# three_in_one = Triple()

# three_in_one.comeback()
# print(three_in_one.spisok)

# номер 2
# Создать класс, описывающий автомобиль (производитель, 
# модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации об автомобиле.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# class Auto():
#     def __init__(self):
#         self.brand = 'bmw'
#         self.model = 'm5'
#         self.year = '2020'
#         self.speed = '150 km/h'
#     def info(self):
#         print(f'Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nSpeed: {self.speed}')
#     def calc(self):
#         self.speed = 150
#         distance = int(input('Введите расстояние: '))
#         total = distance/self.speed
#         print(f'Время для преодоления расстояния равно: {round(total,1)} часов')
        
# bmw_car = Auto()

# bmw_car.info()
# bmw_car.calc()

# номер 3
# создать класс колькулятор 
# в конструкторе нужно в писать 2 числа
# создать 4 метода: умножение , деление , сумма , вычитание
# создать метод для добавления числа (его можно вызвать много раз и подучить много чисел)

class Calc():
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 0
    def input(self, num_1 = 0,  num_2= 0):
        self.num_1 = num_1
        self.num_2 = num_2
    def mult(self):
        return self.num_1 * self.num_2
    def divide(self):
        return int(self.num_1 / self.num_2)
    def add(self):
        return self.num_1 + self.num_2
    def subtract(self):
        return self.num_1 - self.num_2
    

calculator = Calc()

calculator.input(5,5)
print(calculator.mult())
calculator.input(7,7)
print(calculator.divide())
calculator.input(9,9)
print(calculator.add())
calculator.input(12,12)
print(calculator.subtract())

