from tkinter import *
import threading
import keyboard
import time

# Инициализация окна
window = Tk()
window.title("Multi Timer")
window.geometry("100x100")
window.config(bg="#facca6")
window.attributes("-topmost", True)

# Таймеры для кнопок
timers = {"4": 0, "5": 0}
countdown_active = {"4": False, "5": False}

# Метка для отображения таймера
timer_label = Label(window, text="0", bg="#facca6", font=("Arial", 24))
timer_label.pack(expand=True)

# Функция обратного отсчета
def countdown(key):
    global timers, countdown_active
    if timers[key] > 0:
        timers[key] -= 1
        timer_label.config(text=f"{timers[key]}")
        window.after(1000, countdown, key)
    else:
        
        countdown_active[key] = False

# Функция для запуска таймера с задержкой
def start_timer(key):
    global timers, countdown_active
    if key.name in timers:
        delay = 2400 if key.name == "4" else 1900  # Задержка в миллисекундах
        def delayed_start():
            timers[key.name] = 6 if key.name == "4" else 7  # Разные значения для разных кнопок
            timer_label.config(text=f"{timers[key.name]}")
            if not countdown_active[key.name]:
                countdown_active[key.name] = True
                countdown(key.name)
        window.after(delay, delayed_start)

# Функция для глобального отслеживания клавиш
def listen_keys():
    keyboard.on_press(start_timer)

# Запускаем поток для отслеживания клавиш
thread = threading.Thread(target=listen_keys, daemon=True)
thread.start()

# Запуск окна
window.mainloop()