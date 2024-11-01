# дз
# задание 1
# создайте родительский класс , описывающий транспорт
# (модель, год выпуска, средняя скорость), и следующие функции 
# для работы с этим объектом.
# 1. Функция для вывода на экран информации о транспорте.
# 2. Функция для подсчета необходимого времени для преодоления переданного расстояния со средней скоростью.

# наследуйте класс автомобили в котором есть ещё одна переменная количество мест

# наследуйте класс вертолеты с дополнительным методом взлет 

class Transport():
    def __init__(self):
        self.brand = 'bmw'
        self.model = 'm5'
        self.year = '2020'
        self.speed = '150 km/h'
    def info(self):
        print(f'Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nSpeed: {self.speed}')
    def calc(self):
        self.speed = 150
        distance = int(input('Введите расстояние: '))
        total = distance/self.speed
        print(f'Время для преодоления расстояния равно: {round(total,1)} часов')
        
bmw_car = Transport()

bmw_car.info()
bmw_car.calc()

class Auto(Transport):
    def __init__(self):
        super().__init__()
        self.seat = 5

    
class Verolet(Transport):
    def __init__(self):
        super().__init__()
        
    def vzlet(self):
        print('Vzletayy')