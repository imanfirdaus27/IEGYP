#input is a built in function
#which takes a single parameter(caption/question)
# The input function display the caption to the user 
# and take the keyboard input
# assign it to the variable
firstNumber = input("Enter the first number:")
secondNumber = input("Enter the second number:")
print(firstNumber)
print(type(firstNumber))
# if you want to perform arithmetic operation
# this must be converted to a number
firstNumber = int(firstNumber)

secondNumber = int(input("Enter the second number:"))

print(firstNumber + secondNumber)