import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))

array2D = np.array([[1, 2], [3, 4]])
print(array2D)
print(type(array2D))
print(array2D.shape)

zero_array = np.zeros((3, 4), dtype=int)
ones_array = np.ones((3, 4), dtype=int)
fives_array = np.full((3, 4), 5, dtype=int)
random_array = np.random.random((3, 4))

print(zero_array)
print(ones_array)
print(fives_array)
print(random_array)
# print(random_array[0, 0])
print(random_array > 0.2)
print("")
print(random_array[random_array > 0.2])
print(np.sum(random_array))
print(np.floor(random_array))
print(np.ceil(random_array))
print(np.round(random_array))



