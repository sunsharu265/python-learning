
strings and numbers in python
print('Hello world', "It's a beautiful day", 42)
print("Hello world 2")
print('''Hello world 3''')
print('"Beautiful is better than ugly.", Said Tim Peters')

#multi print values in python using comma separated values (csv)
print('Hello world 4', "Hello world 5",     '''Hello 
        world 
        New line comes here 6''')
print(1+3, 2*3, 4/2, 5-1, 2**3, 10%4)

#string contatenation in python using + operator
print('Hello' + ' ' + 'World')
long_string = 'Hello' + 'World without contactenation operator.' + ' World without contactenation operator 2 using space separateor'
print(long_string, len(long_string))

# string functions in python
print('---------------------------------------------')
print(long_string.upper())
print(long_string.lower())
print(long_string.capitalize())
print(long_string.title())
print('Stripe function : ' + long_string.strip())
print(long_string.replace('World', 'Universe'))
print(long_string.split('.'))


# Practice questions for string functions in python

# Common beginner string methods:
# upper(), lower(), title(), capitalize(), strip(), lstrip(), rstrip(),
# replace(old, new), split(separator), join(iterable), find(substring),
# count(substring), startswith(prefix), endswith(suffix), isdigit(), and isalpha().
# Useful built-ins include len(text) and str(value). String methods return new
# strings because strings cannot be changed in place.
#
# To discover methods and learn how to use them:
# print(dir(str))          # lists string methods and attributes
# help(str.replace)        # explains one method
# help(str)                # explains the string type
# You can also search the official Python documentation for "string methods".
#
# Beginner practice questions (write code to solve each one):
# 1. Convert "hello, world" to uppercase.
# 2. Convert "PYTHON IS FUN" to lowercase.
# 3. Convert "learning python" to title case.
# 4. Remove leading and trailing spaces from "  hello  ".
# 5. Replace "bad" with "good" in "This is a bad example".
# 6. Count how many times "a" appears in "bananas".
# 7. Check whether "Python programming" starts with "Python".
# 8. Check whether "notes.txt" ends with ".txt".
# 9. Split "red,green,blue" into a list using the comma as separator.
# 10. Join ["learn", "python", "today"] into one string with spaces.
# 11. Find the position of "code" in "I like to code".
# 12. Check whether "12345" contains only digits and "hello" only letters.
# 13. Ask the user for a sentence and print its length with len().

sentence = input("Enter a sentence: ")
print("The length of the sentence is:", len(sentence))
joinStrong = " ".join(["learn", "python", "today"])
print("Joined string:", joinStrong)


#Practice Assignment

# Generate Password using string functions in python which should contain at least 8 characters, including uppercase letters, lowercase letters, numbers, and special characters. get user input for password criteria and say whether it meets the requirements.

# Generate Word contains Vowels using string functions in python which should contain at least 5 characters, including uppercase letters, lowercase letters, and vowels. get user input for word criteria and say whether it meets the requirements.

# Without using string functions in python, check whether a given string is a palindrome or not. get user input for string and say whether it is a palindrome or not.