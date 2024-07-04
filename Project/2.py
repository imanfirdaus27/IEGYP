# def customerdetails(filepath):
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             customer_dict = ast.literal_eval(content)


#             for customer_id, details in customer_dict.items():
#                 print(f"Customer ID: {customer_id}")
#                 print(f"Name: {details['Name']}")
#                 print(f"Address: {details['Address']}")
#                 print(f"Phone: {details['Phone']}")
#                 print(f"IC No: {details['IC No']}")
#                 print(f"Balance: {details['Balance']}")
#                 print(f"Startdate: {details['Startdate']}")
#                 print(f"Enddate: {details['Enddate']}")
#                 print(f"CarID: {details['CarID']}")
#                 print("=" * 40)
#     except FileNotFoundError:
#         print(f"Error: File '{filepath}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")

# def cardetails(filepath):
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             customer_dict = ast.literal_eval(content)
#             for car_id, details in customer_dict.items():
#                 print(f"Car ID: {car_id}")
#                 print(f"Brand: {details['Brand']}")
#                 print(f"Type: {details['Type']}")
#                 print(f"Plate Number: {details['Plate Num']}")
#                 print(f"Price per day: {details['Price/day']}")
#                 print("=" * 40)
#     except FileNotFoundError:
#         print(f"Error: File '{filepath}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")

import ast

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

            # return details['CarID']
        
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
                print(f"{'Total:RM2000':>80}")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")


customer_id = input("Please enter the customer ID: ")

filename1 = "customerdetails.txt"
customerdetails(filename1, customer_id)

carId = getcarID(filename1,customer_id) #capture the car id from customer details from getID function

filename2 = "carlisting.txt"
cardetails(filename2,carId) # return to cardetails function


# def getID(filepath):
#     with open(filepath, 'r') as file:
#         content = file.read()
#         customer_dict = ast.literal_eval(content)

#         customer_id = input("Please enter the customer ID: ")
#     return customer_id


# next step berapa hari dia pakai
# then kira total