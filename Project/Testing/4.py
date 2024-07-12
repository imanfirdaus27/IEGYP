import ast
from datetime import datetime

def customerdetails(filepath, customer_id):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            if customer_id in customer_dict:
                details = customer_dict[customer_id]

                print("=" * 80)

                title = "SOCAR"
                print(f"{title:^80}")

                title = "RENTAL INVOICE"
                print(f"{title:^80}")

                print("=" * 80)

                title = "CUSTOMER DETAILS"
                print(f"{title:^80}")
                print("=" * 80)

                print(f"{'Name':<15}: {details['Name']}")
                print(f"{'Address':<15}: {details['Address']}")
                print(f"{'Phone':<15}: {details['Phone']}")
                print(f"{'IC No':<15}: {details['IC No']}")
                print(f"{'Startdate':<15}: {details['Startdate']}")
                print(f"{'Enddate':<15}: {details['Enddate']}")
                print("=" * 80)

                # Return the start date and end date for rental period calculation
                return details['Startdate'], details['Enddate']

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def getcarID(filepath, customer_id):
    with open(filepath, 'r') as file:
        content = file.read()
        customer_dict = ast.literal_eval(content)

        if customer_id in customer_dict:
            details = customer_dict[customer_id]
            # Return the CarID associated with the customer
            return details['CarID']

def cardetails(filepath, car_id, rental_days):
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
                print(f"{'Days rent':<15}: {rental_days}")
                print("=" * 80)

                # Remove the "RM" prefix and convert the price per day to a float
                price_per_day_str = details['Price/day'].replace('RM', '').strip()
                price_per_day = float(price_per_day_str)
                
                # Calculate the total rental payment based on the number of rental days
                total_rental_payment = price_per_day * rental_days

                print(f"{'Payment Method:':>80}")
                print(f"{'Grand Total: RM ' + str(total_rental_payment):>80}")
                print(f"{'Deposit: RM ':>80}")
                      
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
    rental_days = (end_date - start_date).days + 1
    return rental_days

def main():
    # Prompt the user to enter the customer ID
    customer_id = input("Please enter the customer ID: ")

    # Filepath to the customer details text file
    filename1 = "customerdetails.txt"
    # Get the start date and end date for the customer's rental period
    start_date, end_date = customerdetails(filename1, customer_id)

    if start_date and end_date:
        # Get the CarID associated with the customer
        carId = getcarID(filename1, customer_id)

        # Calculate the number of rental days
        rental_days = calculate_rental_days(start_date, end_date)

        # Filepath to the car listing text file
        filename2 = "carlisting.txt"
        # Display the car details and calculate the total rental payment
        cardetails(filename2, carId, rental_days)
    else:
        print("Unable to retrieve start date and end date for the rental period.")
    
if __name__ == "__main__":
    main()


