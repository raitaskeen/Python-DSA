#NUMERIC DATA TYPES
#Integer
age = 10
temperature = -5
print(type(age))  # Output: <class 'int'>

#Float
height = 5.5
weight = 50.5
print(type(height))  # Output: <class 'float'>

#Complex
complex_number = 3 + 4j
print(type(complex_number))  # Output: <class 'complex'>

#SEQUENCE DATA TYPES
#String
name = "John"
address = '123 Main St'
print(type(name))  # Output: <class 'str'>

#List
fruits = ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>
print(fruits[0])  # Output: apple

#Tuple
#Tuples are similar to lists, but they are immutable, meaning that the values inside a tuple cannot be changed.
colors = ('red', 'green', 'blue')
print(type(colors))  # Output: <class 'tuple'>
print(colors[0])  # Output: red

#Mapping Data Types
#Dictionary
student = {
    'name': 'John',
    'age': 10,
    'grade': 5
}
print(type(student))  # Output: <class 'dict'>
print(student['name'])  # Output: John

#SET DATA TYPES
#Set
#A set is an unordered collection of unique elements.
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))  # Output: <class 'set'>

#Frozen Set
#A frozen set is an immutable version of a set.
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(type(frozen_numbers))  # Output: <class 'frozenset'>

#BOOLEAN DATA TYPE
#Boolean
is_student = True
is_teacher = False
print(type(is_student))  # Output: <class 'bool'>

#NONE DATA TYPE
#None
#The None data type represents the absence of a value.
empty_value = None
print(type(empty_value))  # Output: <class 'NoneType'>

#CONVERSION BETWEEN DATA TYPES
#Convert from one data type to another
#Convert an integer to a float
age = 10
age_float = float(age)
print(type(age_float))  # Output: <class 'float'>

#Convert a float to an integer
temperature = 5.5
temperature_int = int(temperature)
print(type(temperature_int))  # Output: <class 'int'>

#Convert a string to an integer
number = "10"
number_int = int(number)
print(type(number_int))  # Output: <class 'int'>

#Convert an integer to a string
age = 10
age_str = str(age)
print(type(age_str))  # Output: <class 'str'>

#Convert a list to a tuple
fruits = ['apple', 'banana', 'cherry']
fruits_tuple = tuple(fruits)
print(type(fruits_tuple))  # Output: <class 'tuple'>

#Convert a tuple to a list
colors = ('red', 'green', 'blue')
colors_list = list(colors)
print(type(colors_list))  # Output: <class 'list'>

#Convert a list to a set
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers_set = set(unique_numbers)
print(type(unique_numbers_set))  # Output: <class 'set'>

#Convert a set to a list
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers_list = list(unique_numbers)
print(type(unique_numbers_list))  # Output: <class 'list'>

#Convert a list to a dictionary
student = {
    'name': 'John',
    'age': 10,
    'grade': 5
}
student_list = list(student.items())
print(type(student_list))  # Output: <class 'list'>

#Convert a dictionary to a list
student = {
    'name': 'John',
    'age': 10,
    'grade': 5
}
student_dict = dict(student_list)
print(type(student_dict))  # Output: <class 'dict'>

#Convert a list to a string
fruits = ['apple', 'banana', 'cherry']
fruits_str = ', '.join(fruits)
print(type(fruits_str))  # Output: <class 'str'>

#Convert a string to a list
fruits_str = 'apple, banana, cherry'
fruits = fruits_str.split(', ')
print(type(fruits))  # Output: <class 'list'>

#Convert a string to a set
unique_numbers_str = '1, 2, 3, 4, 5'
unique_numbers = set(unique_numbers_str.split(', '))
print(type(unique_numbers))  # Output: <class 'set'>

#Convert a set to a string
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers_str = ', '.join(unique_numbers)
print(type(unique_numbers_str))  # Output: <class 'str'>

#Convert a string to a dictionary
student_str = "name=John, age=10, grade=5"
student_dict = dict(item.split('=') for item in student_str.split(', '))
print(type(student_dict))  # Output: <class 'dict'>

#Convert a dictionary to a string
student = {
    'name': 'John',
    'age': 10,
    'grade': 5
}
student_str = ', '.join(f"{key}={value}" for key, value in student.items())
print(type(student_str))  # Output: <class 'str'>

#Convert a string to a tuple
colors_str = 'red, green, blue'
colors = tuple(colors_str.split(', '))
print(type(colors))  # Output: <class 'tuple'>

#Convert a tuple to a string
colors = ('red', 'green', 'blue')
colors_str = ', '.join(colors)
print(type(colors_str))  # Output: <class 'str'>

# Summary
# Integer: Whole numbers, positive or negative, without a decimal point.
# Float: Numbers with a decimal point.
# Complex: Numbers with a real and an imaginary part.
# String: Sequences of characters enclosed in quotes.
# List: Ordered, mutable collections of items.
# Tuple: Ordered, immutable collections of items.
# Dictionary: Collections of key-value pairs.
# Set: Unordered collections of unique items.
# Frozen Set: Immutable sets.
# Boolean: Represents True or False.
# None: Represents the absence of a value.
# By understanding these data types, you'll be able to 
# choose the right type for your variables and use them
#  effectively in your Python programs. Keep practicing,
#  and you'll get even better at it!