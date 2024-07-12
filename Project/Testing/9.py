import ast
from datetime import datetime

# Function to retrieve customer details from file
def customerdetails(filepath, customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]
                return details
            else:
                print("Customer ID not found in the database.")
                return None
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to retrieve car ID from file
def getcarID(filepath, customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]
                return details['CarID']
            else:
                print("Customer ID not found in the database.")
                return None
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
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
                price_per_day_str = details['Price/day'].replace('RM', '').strip()
                price_per_day = float(price_per_day_str)
                total_rental_payment = price_per_day * rental_days

                return total_rental_payment, details
            else:
                print("Car ID not found in the database.")
                return None, None
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Function to calculate rental days from start and end dates
def calculate_rental_days(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        rental_days = (end_date - start_date).days + 1
        return rental_days
    except ValueError:
        print("Invalid date format")
        return None

# Function to calculate deposit amount
def calculate_deposit(total_rental_payment):
    return total_rental_payment / 3

# Function to handle credit card payment
def credit_card():
    while True:
        credit_card_no = input("Enter the credit card number: ").replace(" ", "").strip()
        if len(credit_card_no) != 16 or not credit_card_no.isdigit():
            print("Invalid credit card number")
            continue
        name = input("Enter Card Name Holder: ")
        expired_date = input("Enter credit card expired date in format MMYY without '/': ").strip()
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
            cvv = input("Enter CVV number: ").strip()
            if len(cvv) != 3 or not cvv.isdigit():
                print("Invalid CVV number")
            else:
                break
        break

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

        bank_choice = input("Enter choice [1-7]: ").strip()
        if bank_choice.isdigit() and int(bank_choice) in banks:
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(f"Logging in to {banks[int(bank_choice)]} with username '{username}' and password.")
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
            return True, new_balance
        else:
            print("Payment canceled.")
            return False, balance

# Function to update balance in a new file
def update_balance_in_file(customer_id, new_balance_str):
    filename = "updated_customerdetails.txt"
    with open(filename, 'a') as file:
        file.write(f"{customer_id}: {new_balance_str}\n")

# Main function to orchestrate the rental process
def main():
    customer_id = input("Please enter the customer ID: ")
    filename1 = "customerdetails.txt"
    customer_details = customerdetails(filename1, customer_id)

    if customer_details:
        car_id = getcarID(filename1, customer_id)
        if car_id:
            start_date = customer_details['Startdate']
            end_date = customer_details['Enddate']
            rental_days = calculate_rental_days(start_date, end_date)

            filename2 = "carlisting.txt"
            total_rental_payment, car_details = cardetails(filename2, car_id, rental_days)

            if total_rental_payment and car_details:
                deposit_amount = calculate_deposit(total_rental_payment)

                while True:
                    print("Choose your payment method:")
                    print("1. Credit Card")
                    print("2. FPX")
                    payment_method = input("Enter choice [1-2]: ").strip()

                    if payment_method == '1':
                        credit_card()
                        balance = digital_wallet(customer_id)
                        if balance is not None:
                            payment_successful, new_balance = calculate_payment(total_rental_payment, balance)
                            if payment_successful:
                                break
                            else:
                                continue
                    elif payment_method == '2':
                        fpx()
                        balance = digital_wallet(customer_id)
                        if balance is not None:
                            payment_successful, new_balance = calculate_payment(total_rental_payment, balance)
                            if payment_successful:
                                break
                            else:
                                continue
                    else:
                        print("Invalid payment method")

                if payment_successful:
                    print("Payment successful.")
                    new_balance_str = f'RM {new_balance:.2f}'
                    update_balance_in_file(customer_id, new_balance_str)
                else:
                    print("Payment failed.")
            else:
                print("Error retrieving car details.")
        else:
            print("Car ID not found.")
    else:
        print("Customer ID not found.")

if __name__ == "__main__":
    main()