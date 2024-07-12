class Negative(Exception):
    pass
class Positive():
    def __init__(self, number):
        self.number = number

    def checkpositive(self):
        if self.number > 0:
            return True
        else:
            raise Negative("You entered a negative number. Retry!")

try:
    number = int(input("Enter a positive number:\n"))
    positive_number = Positive(number)
    if positive_number.checkpositive():
        print(f"Good! You entered {number}")
    
except Negative as e:
    print(e)

#Hanafi
# def main():
#     while True:
#         try:
#             num = input("Enter a positive integer\n")
#             num = int(num)
#             if num <= 0:
#                 raise ValueError("You entered a negative number. Retry!")
#             else:
#                 print(f"Good! You entered {num}")
#                 break
#         except ValueError as e:
#             print(e)
#             print("")

# if __name__ == "__main__":
#     main()

