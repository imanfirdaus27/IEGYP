# def multhree(number):
#     c = number % 3
#     if c == 0:
#         print("Fizz", end = " ")
#     else:
#         pass
#     return c

# def mulfive(number):
#     c = number % 5
#     if c == 0:
#         print("Buzz", end = " ")
#     else:
#         pass
#     return c

# def multhreefive(number):
#     c = number % 15
#     if c == 0:
#         print("FizzBuzz", end = " ")
#     else:
#         pass
#     return c

# numbers = range(1, 101)

# for number in numbers:
#     if result:
#         result = multhreefive(number)
#         print(result, end=" ")
#     elif result:
#         result = multhree(number)
#         print(result, end=" ")
#     elif result:
#         result = mulfive(number)
#         print(result, end=" ")
#     else:
#         print(number, end=" ")

# modified iman (name variable at caller same as at define function)
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return str(number)  # Convert number to string for consistent type in output

# # Iterate over numbers from 1 to 100
# for number in range(1, 101):
#     print(fizz_buzz(number), end=" ")

# chatgpt (name variable at caller same as at define function)
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)  # Convert number to string for consistent type in output

# Iterate over numbers from 1 to 100
for num in range(1, 101):
    print(fizz_buzz(num), end=" ")