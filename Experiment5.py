a = 25
b = 12.5
c = "Python"
d = True
print("Value:", a, "Type:", type(a))
print("Value:", b, "Type:", type(b))
print("Value:", c, "Type:", type(c))
print("Value:", d, "Type:", type(d))
a = "25"
b = "12.5"
c = 100
x = int(a)
y = float(b)
z = str(c)
print("Integer:", x, type(x))
print("Float:", y, type(y))
print("String:", z, type(z))
print("Boolean:", bool(c))
# Implicit type conversion
a = 10
b = 5.5
c = a + b
print("Implicit Conversion:")
print("Result:", c)
print("Type:", type(c))
# Explicit type conversion
x = "20"
y = int(x)
print("\nExplicit Conversion:")
print("Value:", y)
print("Type:", type(y))
num1 = int(input("Enter first integer: "))
num2 = float(input("Enter second number: "))
print("First number:", num1)
print("Type:", type(num1))
print("Second number:", num2)
print("Type:", type(num2))
print("Sum:", num1 + num2)
# initializing string
s = "1010"
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
s="a"
c = ord(s)
print ("After converting character to integer : ",end="")
print (c)
# Convert ASCII value to characters
a = chr(99)
b = chr(67)
print(a)
print(b)
# printing integer converting to hexadecimal string
c = hex(10)
print ("After converting 10 to hexadecimal string : ",end="")
print (c)
# printing integer converting to octal string
c = oct(10)
print ("After converting 10 to octal string : ",end="")
print (c)
#string functions
var = 'PYTHON INTERPRETER'
print (var.capitalize())
var = 'MitPolytechnic'
print (var.lower())
print (var.upper())
print (var.swapcase())
var = 'welcome to Python programming'
print (var.title())
var='Python'
print (var.islower())
var='PYTHON'
print (var.isupper())
print ('2'.isdigit())
#find(str [,i [,j]])
var="Mit Polytechnic"
str="oly"
print ("\n",var.find(str)) # Finds the starting position of str
var="Mit Polytechnic"
str="Poly"
print (var.find(str,3,9)) #Finds the string between position 3 to 9
var='That is a good example'
str='was'
print ("\n",var.replace('is',str))
var = "This is a good example"
print ("\n",var.split())
var='Print new line\nNextline\nMove again to new line'
print (var.splitlines())
seq=('ab','bc','cd')
str='+'
print (str.join(seq),"\n")
a = -25
b = 4.5678
numbers = [10, 25, 5, 40, 15]
print("Absolute value:", abs(a))
print("Power:", pow(2, 3))
print("Rounded value:", round(b, 2))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
marks = [75, 82, 68, 91, 85]
total = sum(marks)
count = len(marks)
highest = max(marks)
lowest = min(marks)
average = total / count
print("Marks:", marks)
print("Total:", total)
print("Number of Subjects:", count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average:", average)
import math
print (math.e)
n = 25
print("Square Root:", math.sqrt(n))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Factorial:", math.factorial(5))
print("GCD:", math.gcd(24, 36))
A=2
print (math.exp(A))
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))
print("Value of Pi:", math.pi)
def greet():
    print("Welcome to Python Programming")
greet()
def display():
    print("MIT World Peace University")
display()
#Function with Minimum Two Arguments
def addition(a, b):
    result = a + b
    print("Addition:", result)
addition(10, 20)
addition(25, 15)
#Function with Return Value
def addition(a, b):
    result = a + b
    return result
answer = addition(25, 15)
print("Result:", answer)
def sq_no(num):
    return num**2
print(sq_no(5))
print(sq_no(-5))
def student(name, roll_no):
    print("Name:", name)
    print("Roll No:", roll_no)
student("Rahul", 101)
def student(name, roll_no):
    print("Name:", name)
    print("Roll No:", roll_no)
student(roll_no=102, name="Amit")
def greet(name, message="Welcome to Python"):
    print(name, "-", message)
greet("Rahul")
greet("Amit", "Good Morning")
def addition(a, b):
    result = a + b
    return result
answer = addition(25, 15)
print("Result:", answer)
def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    return total, difference, product
x, y, z = calculate(20, 10)
print("Total:", x)
print("Difference:", y)
print("Product:", z)
def calculate():
    x = 10
    y = 20
    print("Sum:", x + y)
calculate()
def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result
print(sum_all(1, 2, 3, 4, 5))
x = 100
def display():
    print("Value of x inside function:", x)
display()
print("Value of x outside function:", x)
x = 100
def display():
    x = 50
    print("Inside function:", x)
display()
print("Outside function:", x)
x = 10
def update():   
    global x
    x = 50
print("Before function call:", x)
update()
print("After function call:", x)
def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = total / 3
    return total, percentage
m1 = int(input("Enter Python marks: "))
m2 = int(input("Enter Data Structure marks: "))
m3 = int(input("Enter Database marks: "))
total, percentage = calculate_result(m1, m2, m3)
print("Total Marks:", total)
print("Percentage:", percentage)
def largest(a, b, c):
    return max(a, b, c)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
result = largest(x, y, z)
print("Largest Number:", result)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Rahul", age=20, city="Pune")
#SCOPE OF VARIABLES
def my_func():
    x = 10
    print("\nValue inside/LOCAL function:",x)
my_func()
x = 20
print("Value outside/GLOBAL function:",x)
#LAMBDA FUNCTION
sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print ("\nValue of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
a = 'mitwpu'
upper = lambda x: x.upper()
print(upper(a))
a = 'MITWPU'
upper = lambda x: x.lower()
print(upper(a))
check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(10))
print(check(-21))
print(check(0))
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 3 == 0, c)
print(list(even))
def zero(n): #here n is formal parameter set to 0
    print(id(n)) #address of n
    n=0
    print(id(n))
a=100 # a is actual parameter
print(id(a)) #address of a
zero(a) # we are passing parameter a to n
print(a) # a is initially 100.After calling function with a ,where you are setting formal parameter to 0 ,what is value of a?
def add(lst):
    print(id(lst))
    lst=[1,2]
    lst.append(0)
    print(lst)
    print(id(lst))
l=[1,2,3]
print(id(l))
add(l)
print(l)
def changeme( mylist1 ):
    print(id(mylist1))
    mylist1= [1,2,3,4] # This would assig new reference in mylist
    print(id(mylist1))
    print ("Values inside the function: ", mylist1)
    return;
# Now you can call changeme function
mylist = [10,20,30]
print(id(mylist))
changeme( mylist )
print ("Values outside the function: ", mylist)