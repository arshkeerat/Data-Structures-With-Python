# Creating a set
numbers = {10, 20, 30, 40, 50}
print("Set:", numbers)
print("Type:", type(numbers))
# Creating a set using set() function
numbers = set([10, 20, 30, 40, 50])
print("Set:", numbers)
# Creating a set from a string
letters = set("PYTHON")
print("Set of characters:", letters)
numbers = {10, 20, 30, 40, 50}
print("Set:", numbers)
# Membership testing
print("Is 30 present?", 30 in numbers)
print("Is 100 present?", 100 in numbers)
# Accessing elements using loop
print("Set elements:")
for x in numbers:
    print(x)
numbers = {10, 20, 30}
print("Original set:", numbers)
# Add one element
numbers.add(40)
print("After add(40):", numbers)
# Add multiple elements
numbers.update([50, 60, 70])
print("After update():", numbers)
numbers = {10, 20, 30, 40, 50}
print("Original set:", numbers)
numbers.remove(30)
print("After remove(30):", numbers)
numbers.discard(40)
print("After discard(40):", numbers)
numbers.pop()
print("After pop():", numbers)
numbers.clear()
print("After clear():", numbers)
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE",
    "percentage": 85.5
}
print("Student Dictionary:")
print(student)
print("Type:", type(student))
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE",
    "percentage": 85.5
}
print("Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Branch:", student.get("branch"))
print("Percentage:", student.get("percentage"))
student = {
"name": "Rahul",
"roll_no": 101,
"branch": "CSE",
"percentage": 85.5
}
print("Original Dictionary:", student)
# Updating existing value
student["percentage"] = 90.5
# Adding a new key-value pair
student["city"] = "Pune"
print("Updated Dictionary:", student)
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE",
    "percentage": 85.5
}
print("Original Dictionary:", student)
# Delete a particular key
del student["branch"]
print("After del:", student)
# Delete and return a particular key
student.pop("percentage")
print("After pop():", student)
# Delete the last inserted key-value pair
student.popitem()
print("After popitem():", student)
# Remove all elements
student.clear()
print("After clear():", student)
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE",
    "percentage": 85.5
}
print("Keys:")
for key in student:
    print(key)
print("\nValues:")
for value in student.values():
    print(value)
print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)
marks = {
    "Python": 85,
    "Data Structure": 90,
    "Database": 78,
    "Computer Network": 88
}
print("Student Marks:")
for subject, mark in marks.items():
    print(subject, ":", mark)
print("Total Marks:", sum(marks.values()))
print("Highest Marks:", max(marks.values()))
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)