from my_package import module1 as m
number = int(input("\nEnter number = "))
print(m.check_prime(number))
print(m.calculate_factorial(number))
from my_package import module2 as m
a, b = map(int, input("Enter two numbers separated by a space: ").split())
print(m.add(a,b))
print(m.mul(a,b))
import math
print(math.sqrt(16))
# Import only the sqrt function from the math package
from math import sqrt
print(sqrt(25))
import numpy as np
a = np.arange(6)
a
a = np.array([2, 3, 4])
a
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
c = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=complex)
c
a = np.arange(15).reshape(3, 5)
a
a.shape
a.ndim
a.dtype.name
a.size
type(a)
a = np.array([20, 30, 40, 50])
print(a)
b = np.arange(4)
print(b)
c=a-b
print(c)
a = np.array([[-1, 2, 0, 4],
[4, -0.5, 6, 0],
[2.6, 0, 7, 8],
[3, -7, 4, 2.0]])
a = a[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", a)