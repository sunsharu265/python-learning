"""Python function examples and beginner practice assignments."""

# Define a function with ``def`` and call it by name.
def greet():
	print("Hello!")

greet()


# Parameters provide input; return sends a result back to the caller.
def add(a, b):
	return a + b

def multiply(a, b):
    return a * b

def areaOfRectangle(length, width):
    return length * width

def areaOfCircle(radius):
    pi = 3.14159
    return pi * radius ** 2


sum_result = add(2, 3)
print("Sum of 2 and 3 is:", sum_result)

multiply_result = multiply(4, 5)
print("Product of 4 and 5 is:", multiply_result)

rectangle_area = areaOfRectangle(10, 5)
print("Area of rectangle is:", rectangle_area)

circle_area = areaOfCircle(3)
print("Area of circle is:", circle_area)


# A default value is used when the caller leaves that argument out.
def greet_person(name, greeting="Hi"):
	return f"{greeting}, {name}!"


print(greet_person("Ava"))
print(greet_person("Ava", greeting="Welcome"))


# Functions can contain conditionals and loops.
def is_even(number):
	return number % 2 == 0


def count_vowels(text):
	vowels = "aeiou"
	count = 0
	for character in text.lower():
		if character in vowels:
			count += 1
	return count


print("Is 8 even?", is_even(8))
print("Vowels in 'Python':", count_vowels("Python"))


# PRACTICE: Replace each ``pass`` with your solution, then try the examples.
def square(number):
	"""Return the number multiplied by itself."""
	pass


def celsius_to_fahrenheit(celsius):
	"""Convert Celsius to Fahrenheit using F = C * 9 / 5 + 32."""
	pass


def find_larger(a, b):
	"""Return the larger of two numbers."""
	pass


def count_words(sentence):
	"""Return the number of whitespace-separated words in sentence."""
	pass


def sum_numbers(numbers):
	"""Return the sum of a list of numbers (0 for an empty list)."""
	pass


# Challenge: ignore spaces and letter case when checking for a palindrome.
def is_palindrome(text):
	"""Return True if text reads the same forwards and backwards."""
	pass


# Suggested tests (uncomment after completing the assignments):
# print(square(5))                         # 25
# print(celsius_to_fahrenheit(0))         # 32.0
# print(find_larger(4, 9))                # 9
# print(count_words("Learn Python today"))  # 3
# print(sum_numbers([1, 2, 3]))            # 6
# print(is_palindrome("Never odd or even"))  # True
