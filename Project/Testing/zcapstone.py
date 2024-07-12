import ast
import datetime

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

cust_data = {}
car_data = {}

def read_data():
    global cust_data, car_data
    try:
        with open('customerdetails.txt', "rt") as cust_detail:
            cust_data = ast.literal_eval(cust_detail.read())

        with open('carlisting.txt', "rt") as car_listing:
            car_data = ast.literal_eval(car_listing.read())

    except Exception as e:
        print("Something went wrong when we print the data:", e)

def display_data(customer_id):
    global cust_data, car_data

    if customer_id in cust_data:
        customer = cust_data[customer_id]
        car_id = customer.get('CarID')
        if car_id in car_data:
            car = car_data[car_id]
            return customer, car
        else:
            print("ID Not Found")
            return None, None
    else:
        print("Invalid Customer ID")
        return None, None
    
def read_customer_id():
    global cust_data
    
    while True:
        customer_id = input("Enter customer ID:").strip()
        if customer_id in cust_data:
            print(customer_id)
            return customer_id
        else:
            print("ID Not Found")

def payment_method(customer_id):
    while True:
        print("-------------------------")
        print("| 1 - Credit Card       |")
        print("| 2 - Digital Wallet    |")
        print("| 3 - Bank Transfer     |")
        print("| 4 - Cash Payment      |")
        print("| 5 - Exit              |")
        print("-------------------------")
        choice = keyboardInput(int, "Choice [1, 2, 3, 4, 5]: ", "Choice must be Integer")
        if (choice == 1):
            credit_card()
            break
        elif (choice == 2):
            digital_wallet(customer_id)
            break
        elif (choice == 3):
            bank_transfer(customer_id)
            break
        elif (choice == 4):
            cash_payment(customer_id)
            break
        elif (choice == 5):
            break
        else:
            print("Please choose your choice within range 0-4 only")

def credit_card():
    while True:
        credit_card_no = keyboardInput(str, "Enter the credit card number(16-digits):", "Credit Card Number must be integer").replace(" ","").strip()
        if len(credit_card_no) != 16 or not credit_card_no.isdigit():
            print("Invalid credit card")
            continue
        name = input("Enter Card Name Holder:")
        try:
            expired_date = keyboardInput(str, "Enter credit card expired date in format MMYY without '/':", "Expired date must be integer").strip()
            if len(expired_date) != 4 or not expired_date.isdigit():
                print("Expired date must be in format MMYY, etc:1224 :")
            
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
                    print("Invalid CVV number (3-Digits)")
                else:
                    break
            break      
        except ValueError:
            return "Invalid expiration date format"
    print("Your payment is successful")

def calculate_payment(customer_id):
    global cust_data, car_data

    if customer_id:
        customer = cust_data[customer_id]
        carid = customer.get('CarID')
        car = car_data[carid]

        start_date = datetime.datetime.strptime(customer['Startdate'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(customer['Enddate'], '%Y-%m-%d')
        price_per_day = float(car['Price/day'].replace('RM', ''))
        balance = float(customer['Balance'].replace('RM', ''))
        day_of_rent = (end_date - start_date).days + 1
        total_payment = day_of_rent * price_per_day

        if balance < total_payment:
            print("Your balance is insufficient. Choose another payment method")
            digital_wallet(customer_id) # nnti tukar back to payment methodz
        
        else:
            new_balance = balance - total_payment
            print("Your payment is successful")
            print(f"Your new account balance: {new_balance}")
            return new_balance

def digital_wallet(customer_id):
    global cust_data

    while True:
        print("----------------------")
        print("| 1 - Shopee Pay     |")
        print("| 2 - Grab Pay       |")
        print("| 3 - TnG            |")
        print("| 4 - Apple Pay      |")
        print("| 5 - Paypal         |")
        print("| 6 - Main Menu      |")
        print("----------------------")
        choice = keyboardInput(int, "Choice [1, 2, 3, 4, 5, 6]: ", "Choice must be Integer")
        if (choice == 1):
            calculate_payment(customer_id)
            break
        elif (choice == 2):
            calculate_payment(customer_id)
            break
        elif (choice == 3):
            calculate_payment(customer_id)
            break
        elif (choice == 4):
            calculate_payment(customer_id)
            break
        elif (choice == 5):
            calculate_payment(customer_id)
            break
        elif (choice == 6):
            payment_method(customer_id)
            break
        else:
            print("Please choose your choice within range 0-5 only")

def username_password(customer_id):
    global cust_data

    username = input("Enter username:\n")
    password = input("Enter password:\n")
    print("\n\n\n")
    print("=============================================")
    print("Username:", username)
    print("Password:", '*' * len(password))
    calculate_payment(customer_id)

def bank_transfer(customer_id):

    while True:
        print("-----------------------")
        print("| 1 - Maybank         |")
        print("| 2 - CIMB            |")
        print("| 3 - Bank Islam      |")
        print("| 4 - RHB             |")
        print("| 5 - BSN             |")
        print("| 6 - Main Menu       |")
        print("-----------------------")
        choice = keyboardInput(int, "Choice [1, 2, 3, 4, 5, 6]: ", "Choice must be Integer")
        if (choice == 1):
            username_password(customer_id)
            break
        elif (choice == 2):
            username_password(customer_id)
            break
        elif (choice == 3):
            username_password(customer_id)
            break
        elif (choice == 4):
            username_password(customer_id)
            break
        elif (choice == 5):
            username_password(customer_id)
            break
        elif (choice == 6):
            payment_method(customer_id)
            break
        else:
            print("Please choose your choice within range 0-5 only")

def cash_payment(customer_id):
    global cust_data

    if customer_id:
        customer = cust_data[customer_id]
        print(f"Your payment is pending. Make sure to pay at the counter before {customer['Startdate']}.")

def main():
    read_data()
    customer_id = read_customer_id()
    if customer_id:
        payment_method(customer_id)
    else:
        print("Failed to read customer data")

main()