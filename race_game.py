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
    def Move_Right(self, e):
        pos = self.Game_Window.coords(self.Player_Car)
        if pos[0] >= 650:
            self.Game_Window.move(self.Player_Car, 0, 0)
            print ('u cant move')
        else:
            self.Game_Window.move(self.Player_Car, self.x, self.y)

    def Move_Left(self, e):
        pos = self.Game_Window.coords(self.Player_Car)
        if pos[0] <= 350:
            self.Game_Window.move(self.Player_Car, 0, 0)
            print ('u cant move')
        else:
            self.Game_Window.move(self.Player_Car, -self.x, self.y)

    def Move_Forward(self, e):
        pos = self.Game_Window.coords(self.Player_Car)
        if pos[1] <= 50:
            self.Game_Window.move(self.Player_Car, 0, 0)
            print ('u cant move')
        else:
            self.Game_Window.move(self.Player_Car, self.xx, -self.yy)

    def Move_Back(self, e):
        pos = self.Game_Window.coords(self.Player_Car)
        if pos[1] >= 850:
            self.Game_Window.move(self.Player_Car, 0, 0)
            print ('u cant move')
        else:
            self.Game_Window.move(self.Player_Car, self.xx, self.yy)

    def __init__(self, Game_Window, window):
        self.Game_Window = Game_Window
        self.window = window
        self.car_image_1 = PhotoImage(file= "NicePng_top-of-car-png_8030690.png")
        self.Player_Car = self.Game_Window.create_image(500,800, anchor = NW, image = self.car_image_1)
        self.Game_Window.move(self.Player_Car, 0, 0)

        self.window.bind("<a>", self.Move_Left)
        self.window.bind("<d>", self.Move_Right)
        self.window.bind("<w>", self.Move_Forward)
        self.window.bind("<s>", self.Move_Back)

        self.x = 50
        self.y = 0
        self.xx = 0
        self.yy = 75


window = Tk()
window.title("window")
window.geometry(f"{1000}x{1000}+{(window.winfo_screenwidth()-1000)//2}+{(window.winfo_screenheight()-1000)//2}")
window.resizable(False, False)
Game_Window = Canvas(window, height = 1005, width = 1005, bg = "#b4b4b4")
Game_Window.place(x = -5, y = -5)
car = Car(Game_Window, window)

window.mainloop()