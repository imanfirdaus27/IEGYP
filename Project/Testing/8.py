import ast
from datetime import datetime

# Function to handle user input with error handling
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

# Function to handle credit card payment
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

# Function to handle FPX payment
def fpx():
    banks = {
        1: "Maybank",
        2: "CIMB",
        3: "Public Bank",
        4: "RHB Bank",
        5: "Hong Leong Bank",
        6: "AmBank",
        7: "Bank Islam"
    }

    while True:
        print("Choose your bank:")
        for key, value in banks.items():
            print(f"{key}. {value}")

        bank_choice = keyboardInput(int, "Enter choice [1-7]:", "Invalid choice")
        if bank_choice in banks:
            username = input("Enter username:")
            password = input("Enter password:")
            print(f"Logging in to {banks[bank_choice]} with username '{username}' and password.")
            # Additional FPX authentication and processing can be added here
            break
        else:
            print("Invalid bank choice")

# Function to retrieve balance from digital wallet
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

# Function to calculate payment and update balance
def calculate_payment(total_rental_payment, balance):
    print(f"Your current account balance: RM {balance:.2f}")

    if balance < total_rental_payment:
        print("Your balance is insufficient.")
        return False, balance
    else:
        confirm = input("Confirm to use payment method? (yes/no): ").strip().lower()

        if confirm == "yes":
            new_balance = balance - total_rental_payment
            print("Your payment is successful")
            print(f"Your new account balance: RM {new_balance:.2f}")
            print("=" * 100)
            print(f"{'Thank you for choosing SOCAR!':^100}")
            print("=" * 100)
            return True, new_balance
        else:
            print("Payment canceled.")
            return False, balance

# Function to retrieve customer details from file
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

                return details['Startdate'], details['Enddate'], details

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

# Function to retrieve car ID from file
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

# Function to retrieve car details from file and calculate total payment
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

                return total_rental_payment, details

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Function to calculate rental days from start and end dates
def calculate_rental_days(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    rental_days = (end_date - start_date).days + 1
    return rental_days

# Function to calculate deposit amount
def calculate_deposit(total_rental_payment):
    return total_rental_payment / 3

# Function to update balance in a new file
def update_balance_in_file(customer_id, new_balance_str):
    filename = "updated_customerdetails.txt"
    with open(filename, 'a') as file:
        file.write(f"{customer_id}: {new_balance_str}\n")

# Main function to orchestrate the rental process
def main():
    customer_id = input("Please enter the customer ID: ")
    filename1 = "customerdetails.txt"
    start_date, end_date, customer_details = customerdetails(filename1, customer_id)

    if start_date and end_date:
        carId = getcarID(filename1, customer_id)
        rental_days = calculate_rental_days(start_date, end_date)
        filename2 = "carlisting.txt"
        total_rental_payment, car_details = cardetails(filename2, carId, rental_days)
        deposit_amount = calculate_deposit(total_rental_payment)

        while True:
            print("Choose your payment method:")
            print("1. Credit Card")
            print("2. E-Wallet")
            print("3. FPX")
            payment_method = keyboardInput(int, "Enter choice [1-3]:", "Choice must be an integer")

            if payment_method == 1:
                credit_card()
                payment_method_name = "Credit Card"
                balance = digital_wallet(customer_id)
                if balance is not None:
                    payment_successful, new_balance = calculate_payment(total_rental_payment, balance)
                    if payment_successful:
                        break
                    else:
                        continue  # Go back to payment method menu
            elif payment_method == 2:
                balance = digital_wallet(customer_id)
                if balance is not None:
                    payment_successful, new_balance = calculate_payment(total_rental_payment, balance)
                    payment_method_name = "E-Wallet"
                    if payment_successful:
                        break
                    else:
                        continue  # Go back to payment method menu
            elif payment_method == 3:
                fpx()
                payment_method_name = "FPX"
                balance = digital_wallet(customer_id)
                if balance is not None:
                    payment_successful, new_balance = calculate_payment(total_rental_payment, balance)
                    if payment_successful:
                        break
                    else:
                        continue  # Go back to payment method menu
            else:
                print("Invalid payment method")

        if payment_successful:
            print("=" * 100)
            print(f"{'SOCAR':^100}")
            print(f"{'RENTAL INVOICE':^100}")
            print("=" * 100)
            print(f"{'CUSTOMER DETAILS':^100}")
            print("=" * 100)
            print(f"{'Name':<20}: {customer_details['Name']}")
            print(f"{'Address':<20}: {customer_details['Address']}")
            print(f"{'Phone':<20}: {customer_details['Phone']}")
            print(f"{'IC No':<20}: {customer_details['IC No']}")
            print(f"{'Startdate':<20}: {customer_details['Startdate']}")
            print(f"{'Enddate':<20}: {customer_details['Enddate']}")
            print("=" * 100)
            print(f"{'RENTAL DETAILS':^100}")
            print("=" * 100)
            print(f"{'Brand':<20}: {car_details['Brand']}")
            print(f"{'Type':<20}: {car_details['Type']}")
            print(f"{'Plate Number':<20}: {car_details['Plate Num']}")
            print(f"{'Price/day':<20}: {car_details['Price/day']}")
            print(f"{'Days rent':<20}: {rental_days}")
            print("=" * 100)
            print(f"{'Grand Total:':<90} RM {total_rental_payment:.2f}")
            print(f"{'Deposit:':<90} RM {deposit_amount:.2f}")
            print(f"{'Payment Method':<20}: {payment_method_name} (PAID)")
            print("=" * 100)

            # Update the customer's balance in a new file
            new_balance_str = f'RM {new_balance:.2f}'
            update_balance_in_file(customer_id, new_balance_str)

            print("Customer balance updated successfully.")
        else:
            print("Payment failed or canceled.")

if __name__ == "__main__":
    main()






