import ast
from datetime import datetime

def keyboardInput(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while isInvalid:
        try:
            if defaultValue is None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if value.strip() == "":
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def credit_card():
    while True:
        credit_card_no = keyboardInput(str, "Enter the credit card number:", "Credit Card Number must be integer").replace(" ", "").strip()
        if len(credit_card_no) != 16 or not credit_card_no.isdigit():
            print("Invalid credit card")
            continue
        name = input("Enter Card Name Holder:")
        try:
            expired_date = keyboardInput(str, "Enter credit card expired date in format MMYY without '/':", "Expired date must be integer").strip()
            if len(expired_date) != 4 or not expired_date.isdigit():
                print("Expired date must be in format MMYY")
                continue
            
            month = int(expired_date[:2])
            year = int(expired_date[2:])
            current_year = datetime.now().year % 100

            if month < 1 or month > 12:
                print("Invalid month in expiry date")
                continue
            if year < current_year or (year == current_year and month < datetime.now().month):
                print("Credit card has expired")
                continue

            while True:
                cvv = keyboardInput(str, "Enter CVV number:", "CVV must be integer").strip()
                if len(cvv) != 3 or not cvv.isdigit():
                    print("Invalid CVV number")
                else:
                    break
            break
        except ValueError:
            return "Invalid expiration date format"

def digital_wallet(customer_id):
    try:
        with open("customerdetails.txt", 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                balance_str = customer_dict[customer_id]['Balance']
                balance = float(balance_str.replace('RM', ''))
                return balance
            else:
                print("Customer ID not found in the database.")
                return None
    except FileNotFoundError:
        print("Error: File 'customerdetails.txt' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate_payment(rental_days, total_rental_payment, balance):
    print(f"Your current account balance: RM {balance:.2f}")

    if balance < total_rental_payment:
        print("Your balance is insufficient.")
        return False
    else:
        confirm = input("Confirm to use e-wallet as payment? (yes/no): ").strip().lower()

        if confirm == "yes":
            new_balance = balance - total_rental_payment
            print("Your payment is successful")
            print(f"Your new account balance: RM {new_balance:.2f}")
            print("=" * 100)
            print(f"{"Thank you for choosing SOCAR!":^100}")
            print("=" * 100)
            return True
        else:
            print("Payment canceled.")
            return False


def customerdetails(filepath, customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]

                print("=" * 100)
                print(f"{'SOCAR':^100}")
                print(f"{'RENTAL INVOICE':^100}")
                print("=" * 100)
                print(f"{'CUSTOMER DETAILS':^100}")
                print("=" * 100)

                print(f"{'Name':<20}: {details['Name']}")
                print(f"{'Address':<20}: {details['Address']}")
                print(f"{'Phone':<20}: {details['Phone']}")
                print(f"{'IC No':<20}: {details['IC No']}")
                print(f"{'Startdate':<20}: {details['Startdate']}")
                print(f"{'Enddate':<20}: {details['Enddate']}")
                print("=" * 100)

                return details['Startdate'], details['Enddate']

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def getcarID(filepath, customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]
                return details['CarID']

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def cardetails(filepath, car_id, rental_days):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            car_dict = ast.literal_eval(content)

            if car_id in car_dict:
                details = car_dict[car_id]

                print(f"{'RENTAL DETAILS':^100}")
                print("=" * 100)
                print(f"{'Brand':<20}: {details['Brand']}")
                print(f"{'Type':<20}: {details['Type']}")
                print(f"{'Plate Number':<20}: {details['Plate Num']}")
                print(f"{'Price/day':<20}: {details['Price/day']}")
                print(f"{'Days rent':<20}: {rental_days}")
                print("=" * 100)

                price_per_day_str = details['Price/day'].replace('RM', '').strip()
                price_per_day = float(price_per_day_str)
                total_rental_payment = price_per_day * rental_days

                print(f"{'Payment Method:':<40} [ ] Cash   [ ] Credit Card   [ ] Debit Card   [ ] E-Wallet")
                print(f"{'Grand Total:':<90} RM {total_rental_payment:.2f}")
                print(f"{'Deposit:':<90} RM ______")
                print("=" * 100)

                return total_rental_payment

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def calculate_rental_days(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    rental_days = (end_date - start_date).days + 1
    return rental_days

def main():
    customer_id = input("Please enter the customer ID: ")
    filename1 = "customerdetails.txt"
    start_date, end_date = customerdetails(filename1, customer_id)

    if start_date and end_date:
        carId = getcarID(filename1, customer_id)
        rental_days = calculate_rental_days(start_date, end_date)
        filename2 = "carlisting.txt"
        total_rental_payment = cardetails(filename2, carId, rental_days)

        while True:
            print("Choose your payment method:")
            print("1. Credit Card")
            print("2. E-Wallet")
            payment_method = keyboardInput(int, "Enter choice [1, 2]:", "Choice must be an integer")

            if payment_method == 1:
                credit_card()
                break
            elif payment_method == 2:
                balance = digital_wallet(customer_id)
                if balance is not None:
                    if calculate_payment(rental_days, total_rental_payment, balance):
                        break
                    else:
                        continue  # Go back to payment method menu
            else:
                print("Invalid payment method")
    else:
        print("Unable to retrieve start date and end date for the rental period.")

if __name__ == "__main__":
    main()
