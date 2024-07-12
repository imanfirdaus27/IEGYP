def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

import datetime

def credit_card():
    while True:
        credit_card_no = keyboardInput(str, "Enter the credit card number:", "Credit Card Number must be integer").replace(" ","").strip()
        # credit = 
        if len(credit_card_no) != 16 or not credit_card_no.isdigit(): # cannot input number with space
            print("Invalid credit card")
            continue
        name = input("Enter Card Name Holder:")# because of string so number bleh msuk jugak
        try:
            expired_date = keyboardInput(str, "Enter credit card expired date in format MMYY without '/':", "Expired date must be integer").strip()
            if len(expired_date) != 4 or not expired_date.isdigit():
                print("Expired date must be in format MMYY")
            
            month = int(expired_date[:2])
            year = int(expired_date[2:])
            current_year = datetime.datetime.now().year % 100

            if month < 1 or month > 12:
                print("Invalid month in expiry date")
                continue
            if year < current_year or (year == current_year and month < datetime.datetime.now().month):
                print("Credit card has expired")
                continue

            while True:
                cvv = keyboardInput(str, "Enter CVV number:", "CVV must be integer").strip()
                if (len(cvv)) != 3 or not cvv.isdigit():
                    print("Invalid CVV number")
                else:
                    break
            break      
        except ValueError:
            return "Invalid expiration date format"
    #    cvv = keyboardInput(int, "Enter CVV number:", "CVV must be integer")
    #   if (len(str(cvv).strip())) != 3
    #        print("Invalid CVV number") # if invalid dia x minta semula


# credit_card()

def digital_wallet():
    choice = -1
    while True:
        print("-----------------")
        print("| 0 - Shopee Pay     |")
        print("| 1 - Grab Pay       |")
        print("| 2 - TnG            |")
        print("| 3 - Apple Pay      |")
        print("| 4 - Paypal         |")
        print("-----------------")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]:", "Choice must be Integer")
        if (choice == 0):
            calculate_payment(2, 1, 110, 120)
            break
        elif (choice == 1):
            calculate_payment(2, 1, 110, 890)
            break
        elif (choice == 2):
            calculate_payment()
            break
        elif (choice == 3):
            calculate_payment()
            break
        elif (choice == 4):
            calculate_payment()
            break
        elif (choice == 5):
            break

def calculate_payment(end_date, start_date, price_per_day, balance):
    # while True:
        day_of_rent = (end_date - start_date) + 1
        total_payment = day_of_rent * price_per_day

        if balance < total_payment:
            print("Your balance is insufficient. Choose another payment method")
            digital_wallet()
        
        else:
            new_balance = balance - total_payment
            print("Your payment is successful")
            print(f"Your new account balance: {new_balance}")
            return new_balance
    
# digital_wallet()
def main ():
    digital_wallet()

if __name__ == '__main__':
    main()

'''
for payment kira total payment first 
kira brapa hari darab price per day
balance ewallet tolak total payment

'''