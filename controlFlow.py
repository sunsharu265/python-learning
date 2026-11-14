"""Beginner examples of Python control flow."""
#if block only 
# age = int(input("Enter your age: "))
# if age > 18:
#     print("You are an adult.")

coinFlip = input("Enter 'heads' or 'tails': ")
# if coinFlip == 'heads':
# 	print("You won!")
# else:
# 	print("You lost!")

coinFlipResult = "You won!" if coinFlip == 'heads' else "You lost!"
print(coinFlipResult)

# if / elif / else: run a block based on a condition.
temperature = int(input("Enter the temperature in Celsius: "))
if temperature > 30:
	print("It's hot.")
elif temperature < 10:
	print("It's cold.")
else:
	print("The weather is mild.")

userEmail = input("Enter your email address: ")
userAccess = input("Enter your access level (admin/user): ")
print("Is 20 < 30? ", 20 != 30)
isAdmin = (userAccess == 'admin')

if userEmail == 'ktkkishore@gmail.com':
	if isAdmin:
		print("Welcome, admin!")
	else:
		print("Welcome, user!")


# for: repeat once for each item in a sequence.
fruits = ["apple", "banana", "orange", 'Grapes', 'Mango', 'Pineapple']

for fruit in fruits:
	print("Fruit:", fruit)

# range(4) gives 0, 1, 2, and 3 (the stop value is excluded).

for number in range(50, 80, 5):
	evenNumber = number % 2 == 0
	if evenNumber:
		print("Even number:", number)
	else:
		print("Odd number:", number)

# while: repeat as long as its condition is True.
count = 1
while count <= 3:
	print("Count:", count)
	count += 1  # Update the value so the loop eventually ends.

# break exits a loop; continue skips to the next iteration.
for number in [1, 2, 3, 4, 5, 6]:
	if number == 2:
		continue
	if number == 5:
		break
	print("Current number:", number)

# Indentation groups statements into blocks. Use consistent indentation.

# Practice Questions
# 1. Write an if/elif/else statement that prints "Freezing", "Mild", or "Warm" based on a temperature value.
# 2. Use a for loop to print every item in the list ["red", "green", "blue"].
# 3. Write a while loop that counts down from 10 to 1 and prints each number.
# 4. Create a loop that skips the number 3 using continue, and stops when a value reaches 10 using break.
# 5. Explain why indentation is required in Python control flow statements.
# 6. Challenge: Use a nested if inside a for loop to print only numbers greater than 5 from the range 1 to 10.

# assignment 1