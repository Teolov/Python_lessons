from array import array
import threading
import time

def arr_sort(arr_loc):
    for i in range(len(arr_loc)):
        for num_index in range(len(arr_loc) -1):
            if(arr_loc[num_index] > arr_loc[num_index + 1]):
                sive_num = arr_loc[num_index]
                arr_loc[num_index] = arr_loc[num_index + 1]
                arr_loc[num_index + 1] = sive_num 
    return arr_loc


thread = threading.Thread(target=arr_sort)

arr = array("i" , [7,3,8,1,8,5,10,5,4])
print(arr)
print(arr_sort(arr))


