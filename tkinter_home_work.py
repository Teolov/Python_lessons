

from tkinter import *
import random


# задача 1
# Создайте игру clicker, при нажатии на кнопку должно число увеличиваться на один

# window = Tk()
# window.title('clicker')
# window.geometry('430x230')
# x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
# y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
# window.wm_geometry("+%d+%d" % (x, y))
# window.config(bg = '#355aff')
# window.resizable(False, False)

# num = 0

# lab_1 = Label(text = num, bg = '#da47b5')
# lab_1.place(width = 200, height = 200, x = 215, y = 15)

# def num_plus():
#     global num
#     num += 1
#     lab_1.config (text = num)
    
# button_num = Button(text= 'click on me', command = num_plus)
# button_num.place(width = 200, height = 200, x = 15, y = 15)

# задача 2
# Сделать игру найди кнопку, при нажатии на кнопку она перемещается в случайное место
# по координатам , но не выходит за границы окна

<<<<<<< HEAD
# window = Tk()
# window.title('finder')
# w, h = 1000, 1000
# window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
# window.config(bg = '#355aff')
# window.resizable(False, False)

# def button_move():
#     button.place(x = random.randint(15,885), y = random.randint(15,885))
    

# def random_color():
#     color = f'#{random.randrange(256**3):06x}'
#     button.config(bg = color)

# def button_changer():
#     button_move()
#     random_color()
    
# button= Button(text= 'click on me', command = button_changer)
# button.place(width = 100, height = 100, x = 15, y = 15)

# entry
# Задание 1. Написать имитацию кассового аппарата для 
# магазина, торгующего новогодними товарами. Кассир 
# должен выбрать товар (кнопки), ввести его количество, 
# затем выбрать следующий товар. По завершению ввода 
# вывести на экран всю сумму покупки.
# В списке товаров должно быть не меньше 
# 4-х товаров, должна отображаться их цена. Предусмотреть 
# неправильно вводимые данные.
# . Хранение общей выручки магазина;
# . Ограничить количество товара в магазине

=======
>>>>>>> e4a800e2b74965f438091e278135c0464a9c78e2
window = Tk()
window.title('finder')
w, h = 1000, 1000
window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
window.config(bg = '#355aff')
window.resizable(False, False)

<<<<<<< HEAD
spisok = []
# функция считающая сумму и добавляющая её в лейб
def summa():
    label_sum.config(text = '1')
# кнопка посчитать
button_summa= Button(text= 'посчитать', command = summa)
button_summa.place(width = 100, height = 115, x = 600, y = 15)
# лейбл с суммой
label_sum = Label(text = '', bg = '#da47b5')
label_sum.place(width = 100, height = 115, x = 475, y = 15)
# инпут 1 товара
inp_1 = Entry()
spisok.append(inp_1.get())
print(spisok)
def b_1():
    inp_1.place(x=15 , y=80 , height=50 , width=100)
# кнопка 1 товара (вызывает инпут)
button_1= Button(text= 'гирлянда = 100р', command = b_1)
button_1.place(width = 100, height = 50, x = 15, y = 15)
# инпут 2 товара
inp_2 = Entry()
def b_2():
    inp_2.place(x=130 , y=80 , height=50 , width=100)
# кнопка 2 товара (вызывает инпут)
button_2= Button(text= 'петарда = 50р', command = b_2)
button_2.place(width = 100, height = 50, x = 130, y = 15)
# инпут 3 товара
inp_3 = Entry()
def b_3():
    inp_3.place(x=245 , y=80 , height=50 , width=100)
# кнопка 3 товара (вызывает инпут)
button_3= Button(text= 'звезда = 75р', command = b_3)
button_3.place(width = 100, height = 50, x = 245, y = 15)
# инпут 4 товара
inp_4 = Entry()
def b_4():
    inp_4.place(x=360 , y=80 , height=50 , width=100)
# кнопка 4 товара (вызывает инпут)
button_4= Button(text= 'елка = 500р', command = b_4)
button_4.place(width = 100, height = 50, x = 360, y = 15)

=======
def button_move():
    button.place(x = random.randint(15,885), y = random.randint(15,885))
    

def random_color():
    color = f'#{random.randrange(256**3):06x}'
    button.config(bg = color)

def button_changer():
    button_move()
    random_color()
    
button= Button(text= 'click on me', command = button_changer)
button.place(width = 100, height = 100, x = 15, y = 15)
>>>>>>> e4a800e2b74965f438091e278135c0464a9c78e2






















window.mainloop()