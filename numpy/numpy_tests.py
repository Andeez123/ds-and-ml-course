import numpy as np

# my_list = [1,2,3]

# arr = np.array(my_list)
# arr1 = np.arange(0,11,2)
# # print(np.zeros(3))
# # print(np.zeros((2,3)))
# print(arr1[1:5])

# arr2 = np.arange(0, 11)
# arr2[0:2] = 100
# print(arr2)

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d[2][0])

bool_arr = arr_2d > 30
print(arr_2d[bool_arr])

arr1 = np.arange(0,11)
print(arr1 / arr1)
