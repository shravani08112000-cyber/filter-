# map()

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers) 


def square(x):
    return x ** 2
numbers = [1, 2, 4, 16, 18, 20]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

def odd(x):
    return x % 2 != 0
numbers = [2,5,8,11,14,17]
odd_numbers = list(map(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

def uppercase(s):
    return s.upper()
strings = ["blue", "red", "purple", "yellow", "green"]
uppercase_strings = list(map(uppercase, strings))
print(uppercase_strings)


def reverse_string(s):
    return s[::-1]
reversed_strings = list(map(lambda x: x[::-1], strings))
print(reversed_strings)


def length(s):
    return len(s)
lengths = list(map(lambda x: len(x), strings))
print(lengths)


# filter()
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


def is_longer_than_five(s):
    return len(s) > 5
strings = ["mango", "banana", "cherry", "grape"]
long_strings = list(filter(lambda x: len(x) > 5, strings))
print(long_strings)


def starts_with_a(s):
    return s.startswith('a')       
strings = ["mounika", "anusha", "priya", "sumya", "anil"]
a_strings = list(filter(lambda x: x.startswith('a'), strings))
print(a_strings)


def is_positive(x):
    return x > 0
numbers = [-3, -1, 0, 2, 4, 6]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(negative_numbers)

def is_palindrome(s):
    return s == s[::-1]     
strings = ["madam", "hello", "racecar", "python", "level"]
palindromes = list(filter(lambda x: x == x[::-1], strings))
print(palindromes)    

# reduce()
from functools import reduce    
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(sum_of_numbers)
print(product_of_numbers)

def max_of_two(x, y):
    return x if x > y else y
numbers = [3, 7, 2, 9, 5]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)

def min_of_two(x, y):
    return x if x < y else y
numbers = [3, 7, 2, 9, 5]
min_number = reduce(lambda x, y: x if x < y else y, numbers)
print(min_number)

def  concat_strings(s1, s2):
    return s1 + s2
strings = ["Hello", " ", "Python", "!"]
concatenated_string = reduce(concat_strings, strings)
print(concatenated_string)

def logical_and(x, y):
    return x and y
bools = [True, True, False, True]
result = reduce(lambda x, y: x and y, bools)    
print(result)


