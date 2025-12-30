#import NumPy
import numpy as np

#creating NumPy arrays
arr1 = np.array([10, 20, 30, 40])

print(arr1)
print(type(arr1))

#array with different dimensions
#1D array
a = np.array([1, 2, 3])
print(a)

#2D array

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

#checking array properties
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)     
print(arr.shape)    
print(arr.size)     
print(arr.dtype) 
   
#accessing elements
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr[0, 1])   # 20
print(arr[1, 2])   # 60

#slicing NumPy arrays

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[::-1])

#special arrays
print(np.zeros((2, 3)))
print(np.ones((3, 2)))
print(np.eye(3)) # Identity matrix

#using arange() and linspace()

#mathematical operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#statistical functions
arr = np.array([10, 20, 30, 40])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))