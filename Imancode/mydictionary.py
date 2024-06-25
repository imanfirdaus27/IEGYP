# Python dictionary is also called JSON in other languages
# JSON - Javascript object notation
# Dictionary is represented using {}
# Dictionary is ordered (retain its position)
# Dictionary is index using key(s) (not using numbers 0, 1, 2, 3, 4...)
# Dictionary does not allow duplicate keys but allow duplicate values
# Every data is associated with a key
# Here firstname is a key and peter is a value''
# value can be either list, tuple, another dictionary


foreigner = {
    "firstname": "Peter",
    "lastname": "Parker",
    "passportnumber": "E4854754",
    "incometaxnumber": "SG3843934",
    "last month": 5,
    "last year": 2024,
    "lastamount": 854
    "transaction": [(4, 2024, 852)]
}

print()


# dictionary is modifiable
# how to add a new key

foreigner["car"] = 25
print(foreigner)



