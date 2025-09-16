import numpy as np
arr=np.array([10,20,30,40])
print("Array",arr)

print("Maximum element", np.max(arr))

a=np.array([10,20,30,40])
b=np.array([50,60,70,80])

add=a+b
print(add)

#List
data=[10,20,30,40]
print("multiple ", data*2)

#convert arr-1D to 2D array
arr_1D = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print("2D Array ",arr_1D)

#Transpose of 2D array
arr_1D = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3).T
print("2D Array ",arr_1D)

#Automatic array genertor 
arr=np.arange(1,11)
print(arr)

#Zeros
zero=np.zeros((3,3))
print("Zeros Array")
print(zero)

#Ones
one=np.ones((3,3))
print("Ones Array")
print(one)