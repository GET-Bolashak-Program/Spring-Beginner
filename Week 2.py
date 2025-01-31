# use comments for notes

## numbers

## two kinds of numbers:
## integers and floats

print(5) #integer or int
print(-7)
## floats
print(4.0)
print(4.2)
print(0.4)

## numerical operators
print(2 + 4)
print(2 + .5)

## text, we save as strings

print("hello")
print("2.5")

# operator overloading
## will have multiple definitions

print(2 + 2.4) # + sees numbers? do math
print("cat" + "cat") # str + str makes concatenation

# print(1 + "cat") # type error

print("will you run more?")

# python isn't exactly math...

## won't work....
# print(3 (2 + 4))
## but this will
print(3 * (2 + 4))

# variables

my_number = 10
total = 0

## strings

## use '' "" """"""

print("this works")
print('the same')
print("""even this

fun!
""")

first = "Elizabeth"
second = 'Wickes'

print(first + " " + second)
print(second + ", " + first)

## let's work with dates

date_as_text = "January 31, 2025"
# type() function to check data type
print(type(date_as_text))

# normally we would import things at
# the very beginning
import math
import pandas as pd

print(type(pd))

# let's load a date from a string
# and into a date object

time = pd.Timestamp('10:40:00')
print("our time is...")
print(time)

day_and_time = pd.Timestamp('May 3, 2024 10:03:00')
print(day_and_time)

start = pd.Timestamp('Jan 24, 2025 10:00:00')
today = pd.Timestamp('Jan 31, 2025 10:45:00')
print(start, today)
# print(today - start)
# save it instead
time_diff = today -start
print(time_diff, type(time_diff))
# you can ask for specific things, if the object knows
print(time_diff.days)
print(time_diff.components)
print(time_diff.seconds)

## collecting data together

## hold things together as a sequence
## lists and tuples

## coordinates

coords = (50, -40)
print(coords, type(coords))

## lists
## create one with list() or []

my_list = []
print(type(my_list), len(my_list))
# add things in with append
# no assignment statements with this
my_list.append(10)
my_list.append(-0.8)
my_list.append(10000)
print(my_list)
# both lists and tuples have an order
print(my_list[0]) #access individual items by index
print(my_list[0], my_list[2], my_list[1])

# asking for a single number is indexing

# but if we wanted a collection/sample from inside
# we would use slicing
# start:stop
# start is inclusive, stop is exclusive
# sort of like [0,2)
print(my_list[0:2]) # include the 0 and 1th

# make a larger list of numbers
# range() function to generate number sequences
print(range(100)) # this gives a generator thing
print(list(range(100))) # this lets you see them

nums = list(range(100))

print(nums[20:45])
# other tricks
nums.reverse()
print(nums)

# caution!
# nums = nums.reverse() # no assignment!
nums.reverse() # use it like this
print(nums)

# python dicts
# key/value or mapping objects

my_data = {} # make an empty dict
#add a value
my_data['student_count'] = 15
my_data['room_number'] = "3070"
print(my_data)