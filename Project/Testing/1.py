

# def printDetails(filename):
#     try:
#         with open(filename, "rt") as filehandler:
#             lines = filehandler.readlines()
#         invoiceno = ""
#         for index, line in enumerate(lines):
#             name, address,  = line.strip().split("|")
#             if (index == 0):
#                 print(f"{"No:":<5}{product:20}{quantity:>20}{price:>20}")
#                 print("=" * 80)
#             else:
#                 print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
#     except Exception as e:
#         print("Something went wrong when we print the products", e)


#usingkey
# def customerdetails(filename):
#     try:
#         with open(filename, "rt") as file:
#             lines = file.readlines()
#     except Exception as e:
#         print("Something went wrong when we print the details:", e)

# def customerdetails(filepath):
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             print(f"Name: {content["Name"]}")
#             print(f"Address: {content["Address"]}")
#             print(f"Phone: {content["Phone"]}")
#             print(f"IC No: {content["IC No"]}")
#             print(f"Balance: {content["Balance"]}")
#             print(f"Startdate: {content["Startdate"]}")
#             print(f"Enddate: {content["Enddate"]}")
#             print(f"CarID: {content["CarID"]}")

#     except FileNotFoundError:
#         print(f"Error: File '{filepath}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")

# def cardetails(filepath):
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print(f"Error: File '{filepath}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")


# def printcustomer():
#     x = int(input("Please input the invoice no.:"))

import ast

def customerdetails(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: {e}")


filename1 = "customerdetails.txt"
filename2 = "carlisting.txt"
customerdetails(filename1)
# cardetails(filename2)
# printcustomer(filename1)

