

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

window = Tk()
window.title('finder')
w, h = 1000, 1000
window.geometry(f"{w}x{h}+{(window.winfo_screenwidth()-w)//2}+{(window.winfo_screenheight()-h)//2}")
window.config(bg = '#355aff')
window.resizable(False, False)

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






















window.mainloop()