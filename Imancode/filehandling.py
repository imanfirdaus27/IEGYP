#open('fruits.txt')
# we have to give instruction to python if the does not
# exist create it
# Mode
# 1. x create the file if it does not exist'
# 2. t this is going to be a text file
# 3. b this is going to be a binary file
# open('fruits.txt', 'xt')
# when you run it again we get an error and its File already exists

# The line from os.path import exists is used to import 
# the exists function from the os.path module in Python. 
# The exists function is used to check if a given path (file or directory) 
# exists in the file system.

from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(filename):
    choice = -1
    while (choice != 0):
        print("--------------")
        print("|  0 - Exit  |")
        print("|  1 - List  |")
        print("|  2 - Add   |")
        print("|  3 - Edit  |")
    
        choice = keyboardInput(int, "Choice[0,1,2,3]:", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
        elif (choice == 1):
            printProducts(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)


filename = "fruits.txt"
# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')
# def createFile(filename):
#     if not exists(filename):
#         try:
#             filehandler = open(filename, "xt")
#         except Exception as e:
#             print("Something went wrong when we try to create the file:", e)
#         else:
#             createTitle(filename)
#         finally:
#             # filehandler is an object/instance of file class
#             # filehandler has many method like read, write and close
#             filehandler.close()

def createFile(filename):
    if not exists(filename):
        try:
            with open(filename, "xt") as filehandler:
                createTitle(filehandler)
        except Exception as e:
            print("Something went wrong when we try to create the file:", e)

# whenever you comeout with block the resource will be closed automatically
# def createTitle(filename):
#     try:
#         with open(filename, 'wt') as filehandler:
#             # here | (pipe) is used as delimiter
#             # it will seperate the data
#             # we can use deliiter to split the line into
#             # multiple data
#             filehandler.write("Product|Quantity|Price")
#     except Exception as e:
#             print("Something went wrong when we create the header:", e)
def createTitle(filehandler):
    try:
        filehandler.write("Product|Quantity|Price\n")
    except Exception as e:
        print("Something went wrong when we create the header:", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product:", "Product must be string")
        quantity = keyboardInput(int, "Quantity:", "Quantity must be integer")
        price = keyboardInput(float, "Price:", "Price must be float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)

# def printProducts(filename):
#     try:
#         lines = None
#         with open(filename, "rt") as filehandler:
#             lines = filehandler.readlines()
#         for index, line in enumerate(lines): # tanya yang ni
#             product,quantity, price = line.strip().split("|") # this is good .. revise this
#             if ( index == 0):
#                 print(f"{"No.":5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
#                 print("="*80)
#             else:
#                 print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
#     except Exception as e:
#         print("Something went wrong when we print the products:", e)

def printProducts(filename):
    try:
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if index == 0:
                print(f"{'No.':<5}{product:20}{quantity:>20}{price:>20}")
                print("="*60)
            else:
                print(f"{index:<5}{product:20}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we print the products:", e)

def  editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please keyin index of the Product:", "Index must be Integer")
        if (index > len(data)):
            print("Sorry product not available")
            print("Are you sure you want to edit this product")
            confirm = keyboardInput(str, "Are you sure to edit this product (y/n) ?",  "Please keyin y or n")
            if (confirm == "y"):
                print("Let us edit")
        else:
            product, quantity, prices = data[index]
            print(f"Product:{product}|nQuantity:\n{quantity}\nPrices:{prices}")
        
    except Exception as e:
        print("Something went wrong when we edit the products:", e)

filename = "fruits.txt"
createFile(filename)
doMenu(filename)
# addProduct(filename)
# printProducts(filename)












