colors = ["red", "green", "blue"]
for color in colors:
    print("color:", color)

for i in range(1,11):
	if i>=5 and i<=10:
		print(i)
print ("countdown:")
countdown= 10
while countdown >= 1:
    print(countdown)
    countdown -=1        
for i in range(1,10):
	if i==3:
		continue
	if i==10:
		break
	print(i)   	
def square(number):
	return number **2
print(square(5))
print(square(10))
def celsius_to_fahrenheit(celsius):
	fahrenheit =(celsius  *9/5) +32
	return fahrenheit
print(f"{celsius_to_fahrenheit(25)}")
def find_largest(numbers):
	largest_num =max(numbers)
	smallest_num=min(numbers)
	return largest_num, smallest_num
numbers=[1,2,3,4,5,6,7,8,9]
print(find_largest(numbers))
def calculate_sum ():
	sum_num = ('1,2,3')
	sum_num = (1*2*3)
	return sum_num
print(calculate_sum())

newword = input("enter a word:")
clean_text = newword.replace("madam","madam").lower()
if clean_text==clean_text[::-1] :
    # print("it is palindrome")
    print("true")
else : 
	# print("it is not palindrome")
	print("false")
