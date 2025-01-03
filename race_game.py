# этапы игры:
# 1. движение управляемой машины влево и вправо
# 2. движение других машин
# 3. столкновение = окончание игры
# 4. прогрессия игры = ускорение движения автомобилей
# 5. система очков (побить рекорд)
# 6. интерфейс
# 7. дизайн (спрайты)

from tkinter import *
import time

class Car:
    def __init__(self, Game_Window):
        self.Game_Window = Game_Window
        self.car_image_1 = PhotoImage(file= "NicePng_top-of-car-png_8030690.png")
        self.Player_Car = self.Game_Window.create_image(500,500, image = self.car_image_1)
        # self.Game_Window.move(self.Player_Car)

window = Tk()
window.title("window")
window.geometry(f"{1000}x{1000}+{(window.winfo_screenwidth()-1000)//2}+{(window.winfo_screenheight()-1000)//2}")
window.resizable(False, False)
Game_Window = Canvas(window, height = 1005, width = 1005, bg = "#b4b4b4")
Game_Window.place(x = -5, y = -5)
car = Car(Game_Window)

window.mainloop()