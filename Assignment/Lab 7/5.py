'''
Your task is to Validate Credit Card Number

Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

The task is to check if a given string is valid

Valid credit card number

4539 3195 0343 6467

The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

4_3_ 3_9_ 0_4_ 6_6_

If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:

8569 6195 0383 3437

Then sum all of the digits:

8+5+6+9+6+1+9+5+0+3+8+3+3+4+3+7 = 80

If the sum is evenly divisible by 10, then the number is valid. This number is valid!

'''
class Card:
    def __init__(self, card_number):
        self.card_number = card_number

    def validCreditCard(self):
        card_number = self.card_number.replace(" ", "")
        
        # Check if it is digit or not
        if len(card_number) != 16 or not card_number.isdigit():
            print("Invalid Credit Card Number")
            return None

        card_number = list(map(int, card_number))
        total = 0

        for i in range(len(card_number) - 2, -1, -2):
            a = card_number[i] * 2
            if a > 9:
                a -= 9
            card_number[i] = a

        total = sum(card_number)
        return total

    def __str__(self):
        total = self.validCreditCard()
        if total is None:
            return "Invalid Credit Card Number"
        elif total % 10 == 0:
            return "Valid Credit Card Number"
        else:
            return "Invalid Credit Card Number"

# Example usage
y = input("Enter Credit Card Number: ")
x = Card(y)
print(x)