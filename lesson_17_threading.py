import threading
import time

def fun_1():
    print('start fun')
    time.sleep(5)
    print('end fun')

thread_1 = threading.Thread(target=fun_1)
thread_1.start()


for i in range(10):
    print(i)