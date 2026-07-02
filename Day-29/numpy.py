
import numpy as np
'''
arr1 = np.array([1,2,3,4,5])
print("1-dim",arr1,sep='\n',end='\n\n')

arr2 = np.array([[1,2,3], [4,5,6]])
print("2-dim",arr2,sep='\n',end='\n\n')

arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print("3-dim",arr3,sep='\n',end='\n\n')

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
'''

zeros = np.zeros((4,2))
print(zeros)

identity = np.eye(7)
print(identity)

full_array = np.full((2,3),100)
print(full_array)

range_arr = np.arange(1,43,2)
print(range_arr)

line_space = np.linspace(50,100,6)
print(line_space)

np.random.seed(10)
rand_arr = np.random.randint(6)
print(rand_arr)

rand_int = np.random.randint(1,100,10)
print(rand_int)

rand_float = np.random.rand(3,2)
print(rand_float)

rand_int = np.random.randint(1,6,(5,5))
print(rand_int)

l = ['html','css','js','reactjs','redux']
rand_choice = np.random.choice(l,4)
print(rand_choice)

arr = np.array([[1,2], [4,5], [6,7], [8,7], [1,2], [4,5]])
print(arr.shape)

reshaped = arr.reshape(4,3)
print(reshaped)

a = np.array([[1,2,3,4],[1,2,3,4]])
flattend = a.flatten()
print(flattend)

transposed = arr.T
print(transposed)

arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
print(arr[2:4])
print(arr[:3])
print(arr[::4]) 

matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix[0,1])
print(matrix[2,2])
print(matrix[1,2])
print(matrix[1:,1:])
print(matrix[0:2,1:])

arr = np.array([10,20,30,40,50])

print(arr+10)
print(arr-10)
print(arr*10)
print(arr/10)
print(np.sqrt(arr))

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))

a = np.array([1,2,3,4,5])

print(np.mean(a))
print(np.var(a))
print(np.std(a))

print(np.min(arr))
print(np.max(arr))

arr = np.array([1,2,3,4,5])
print(np.cumsum(arr)) #[1,3,6,10,15]
print(np.cumprod(arr)) #[1,2,6,24,120]

arr = np.array([10,20,30,40,50])

print(arr%20==0)
print(arr[arr%20==0])

arr = np.array([3,1,4,1,5,9,2,6])
sorted_arr = np.sort(arr)
print(sorted_arr)

unique_vals = np.unique(arr)
print(unique_vals)