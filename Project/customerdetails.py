import ast

def customerdetails(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            customer_dict = ast.literal_eval(content)

            customer_id = input("Please enter the customer ID: ")

            if customer_id in customer_dict:
                details = customer_dict[customer_id] 
                print(f"Customer ID: {customer_id}")
                print(f"Name: {details['Name']}")
                print(f"Address: {details['Address']}")
                print(f"Phone: {details['Phone']}")
                print(f"IC No: {details['IC No']}")
                print(f"Balance: {details['Balance']}")
                print(f"Startdate: {details['Startdate']}")
                print(f"Enddate: {details['Enddate']}")
                print(f"CarID: {details['CarID']}")
                print("=" * 40)
            else:
                print(f"Customer ID '{customer_id}' not found.")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")

filename1 = "customerdetails.txt"
customerdetails(filename1)