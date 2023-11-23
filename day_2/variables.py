# Day 2: 30 days of python programming

first_name = 'Ahmad'
last_name = 'Saad'
full_name = 'Ahmad Saad'
country = 'Nigeria'
city = 'Kaduna North'
age = '27'
year = '1996'
is_married = False
is_true = 'Yes'
is_light_on = 'No'

# Declaring multiple variables in one line
interests, hobby, favorite_color = 'football, coding', 'reading', 'blue'

# Exercise level 2
# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(hobby))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3. Compare the length of your first name and your last name
print(len(last_name) < len(first_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one/num_two 
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# 5. The radius of a circle is 30 meters
import math
area_of_circle = math.pi * 30 ** 2
circum_of_circle = math.pi * 2 * 30
radius =  input('radius of circle: ')
area = math.pi * (int(radius)**2)
print(area)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your nationality: ')
age = int(input('Enter your age: '))

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')