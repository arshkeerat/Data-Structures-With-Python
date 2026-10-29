numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
arr = [10, 20, 30, 40, 50]
total = 0
for val in arr:
    total += val
print("Sum =", total)
arr = [10, 20, 30, 40, 50]
arr = [12, 45, 23, 51, 19, 8]
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num
print("Maximum Element:", max_val)
student = {"name": "Mrunal", "age": 21, "marks": 92}
for key, value in student.items():
    print(key, ":", value)
string = "Python"
reversed_str = ""
for ch in string:
    reversed_str = ch + reversed_str
print("Reversed:", reversed_str)
arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)
arr = [4, 7, 1, 9, 3]
key = 9
found = False
for val in arr:
    if val == key:
        found = True
        break
print("Element Found!" if found else "Not Found")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
num = 10
if num > 0:
    print("Positive number")
num = -5
if num >= 0:
    print("Positive number")
else:
    print("Negative number")
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is zero or negative")
a, b, c = 10, 25, 15
if a > b:
    if a > c:
        print("Largest:", a)
    else:
        print("Largest:", c)
else:
    if b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)
num = 30
if num % 2 == 0:
    if num % 5 == 0:
        print("Even and divisible by 5")
    else:
        print("Even but not divisible by 5")
else:
    print("Odd number")
arr = [3, 8, 1, 9, 5]
key = 9
found = False
for val in arr:
    if val == key:
        found = True
        break
if found:
    print("Element Found")
else:
    print("Element Not Found")
for i in range(1, 4): # Outer loop for rows
    for j in range(1, 4): # Inner loop for columns
        print(j, end=" ")
    print() # Move to next line after inner loop
# Program 1: Right-Angled Triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Program 2: Inverted Triangle
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Program 3: Number Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Program 4: Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="") # Spaces
    print("* " * i)
# Program 6: Alphabet Triangle
ch = 65 # ASCII for 'A'
for i in range(5):
    for j in range(i + 1):
        print(chr(ch), end=" ")
    ch += 1
    print()
# Program 7: Floyd's Triangle
num = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
# Program 8: Diamond Pattern
rows = 5
# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
for num in range(1, 11):
    if num % 3 == 0:
        continue # Skip multiples of 3
    print(num)
for letter in "PYTHON":
    if letter == "H":
        pass # Placeholder — no action for 'H'
        print("Pass block executed for letter:", letter)
    print("Current letter:", letter)