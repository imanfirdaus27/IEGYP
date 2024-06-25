norom = {0: "", 1: "i", 2: "ii", 3: "iii", 4: "iv", 5: "v", 
       6: "vi", 7: "vii", 8: "viii", 9: "ix", 
       10: "x", 50: "l", 100: "c", 500: "d", 1000: "m"}

noint = {
    "i": 1, "iv": 4, "v": 5, "ix": 9, "x": 10, "xl": 40, "l": 50,
    "xc": 90, "c": 100, "cd": 400, "d": 500, "cm": 900, "m": 1000
}

def romantointeger(s):
    num = 0
    prev_value = 0
    for char in s[::-1]:  # Process each character in reverse order
        value = noint[char]
        if value < prev_value:
            num -= value
        else:
            num += value
        prev_value = value
    return num


def integertoroman(a):
    words = ""
    
    if a >= 1000:
        while a >= 1000:
            words += norom[1000]
            a -= 1000
    
    if a >= 500:
        while a >= 500:
            words += norom[500]
            a -= 500

    if a >= 100:
        while a >= 100:
            words += norom[100]
            a -= 100
    
    if a >= 50:
        while a >= 50:
            words += norom[50]
            a -= 50
    
    if a >= 10:
        while a >= 10:
            words += norom[10]
            a -= 10
    
    if a > 0:
        words += norom[a]
    
    return words

number = input("Enter 1 for Integer to Roman or 2 for Roman to Integer: ")

if number == "1":
    a = int(input("Enter an integer: "))
    print(integertoroman(a))

elif number == "2":
  s = input("Enter Roman Numeral : ").lower()
  print(romantointeger(s))


















# choice = input("Enter 1 for Roman to Integer, 2 for Integer to Roman: ")
    
# if choice == '1':
#     roman_numeral = input("Enter a Roman numeral: ").upper()
#     integer_value = romantoint(roman)
#     print(f"The integer value of {roman_numeral} is {integer_value}")
# elif choice == '2':
#     integer_value = int(input("Enter an integer: "))
#     roman_numeral = inttoroman(num)
#     print(f"The Roman numeral representation of {integer_value} is {roman_numeral}")

#iman code
# rom = ["", "i","ii","iii","iv","v","vi","vii","viii","ix","x","c","d","m"]
# num = ["",1,2,3,4,5,6,7,8,9,10,100,500,1000]

# def integertoroman(a):
#     words = ""
#     if a >= 1000:
#        while a >= 1000: 
#         words = words + rom[13]
#         a = a - 1000
    
#     if a >= 100:
#        while a >= 100: 
#         words = words + rom[12]
#         a = a - 100

#     if a >= 10:
#        while a >= 10: 
#         words = words + rom[10]

#     if a >= 1 and a <= 9:
#         words = words + rom[a]
    
#     return words

# number = input("Integer(1) or Roman numeral(2): \n")

# if number == "1":
#   a = int(input("Enter Number : "))
#   print(integertoroman(a))