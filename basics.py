print('=============================================')
print('===========  Python Funcdamentals  ==========')
print('=============================================')

# define main function to print out something To know how intentation works in python
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()

print('---------------------------------------------')
#To know Keywords in Python
import keyword

print(keyword.kwlist) 

print('---------------------------------------------')


print('---------------------------------------------')

#variables in python
x = 10
name = "John"
age = 25
#snake case variable name
date_of_birth = "1998-01-01"
#camel case variable name
dateOfBirth = "1998-01-01"

#number in variable name, not recommended to use in first character of variable name, but can be used in middle or end of variable name
firstName323 = "John"

print('Value of date_of_birth : ', date_of_birth)
print('Value of x : ', x)
print('Value of name : ', name)
print('Value of age : ', age)
print('Value of dateOfBirth : ', dateOfBirth)
print('Value of firstName323 : ', firstName323)

# except = 5 #except is a keyword in python, so it cannot be used as variable name;
# print(except) #this will throw an error

#keywords passed as literal string can be used as variable name Example
isMale = False
print(isMale)
