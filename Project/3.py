import ast
from datetime import datetime

def customerdetails(filepath,customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]

                print("=" * 80)

                title = "CUSTOMER DETAILS"
                print(f"{title:^80}")
                print("=" * 80)

                # print(f"Name: {details['Name']}")
                # print(f"Address: {details['Address']}")
                # print(f"Phone: {details['Phone']}")
                # print(f"IC No: {details['IC No']}")
                # print(f"Balance: {details['Balance']}")
                # print(f"Startdate: {details['Startdate']}")
                # print(f"Enddate: {details['Enddate']}")

                print(f"{'Name':<15}: {details['Name']}")
                print(f"{'Address':<15}: {details['Address']}")
                print(f"{'Phone':<15}: {details['Phone']}")
                print(f"{'IC No':<15}: {details['IC No']}")
                print(f"{'Balance':<15}: {details['Balance']}")
                print(f"{'Startdate':<15}: {details['Startdate']}")
                print(f"{'Enddate':<15}: {details['Enddate']}")

                print("=" * 80)

            return details['Startdate'], details['Enddate']
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def getcarID(filepath,customer_id):
    with open(filepath, 'r') as file:
        content = file.read()
        customer_dict = ast.literal_eval(content)

        if customer_id in customer_dict:
            details = customer_dict[customer_id]
            return details['CarID']
   

def cardetails(filepath, car_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            car_dict = ast.literal_eval(content)

            if car_id in car_dict:
                details = car_dict[car_id]

                title = "RENTAL DETAILS"
                print(f"{title:^80}")
                print("=" * 80)

                print(f"{'Brand':<15}: {details['Brand']}")
                print(f"{'Type':<15}: {details['Type']}")
                print(f"{'Plate Number':<15}: {details['Plate Num']}")
                print(f"{'Price/day':<15}: {details['Price/day']}")
                print("=" * 80)
                
                price_per_day = float(details['Price/day'])
                total_rental_payment = price_per_day * rental_days

                print(f"{'Total: RM ' + str(total_rental_payment):>80}")


                print("=" * 80)

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def calculate_rental_days(start_date, end_date):
    # Convert start and end dates from strings to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    # Calculate the number of days between start date and end date
    rental_days = (end_date - start_date).days
    return rental_days



customer_id = input("Please enter the customer ID: ")

filename1 = "customerdetails.txt"
customerdetails(filename1, customer_id)

start_date, end_date = customerdetails(filename1, customer_id)

carId = getcarID(filename1,customer_id) #capture the car id from customer details from getID function

rental_days = calculate_rental_days(start_date, end_date)

filename2 = "carlisting.txt"
cardetails(filename2,carId,rental_days) # return to cardetails function
