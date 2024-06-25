'''
numbers = input("Please enter one or more numbers (separated by commas): ")

liststrnumbers = numbers.split(',')
print(f"List of numbers: {liststrnumbers}" )

listnumbers = []

for num in liststrnumbers:
    listnumbers.append(int(num))

listuniquenumbers = []
    
for num in listnumbers:
    if num not in listuniquenumbers:
        listuniquenumbers.append(num)
print(f"List of unique numbers: {listuniquenumbers}" ) #check satu satu nombor


for num1 in listuniquenumbers:
    found = False
for i in range(len(listuniquenumbers)):
    for j in range(i + 1, len(listuniquenumbers)):
        for k in range(j + 1, len(listuniquenumbers)):
            outputvariable1 = listuniquenumbers[i]
            outputvariable2 = listuniquenumbers[j]
            outputvariable3 = listuniquenumbers[k]
            if outputvariable1 + outputvariable2 + outputvariable3 == 100:
                found = True
                print(f"The three numbers are: {outputvariable1}, {outputvariable2}, and {outputvariable3}")
                break
        if found:
            break
    if found:
        break

if not found:
    print("No three numbers add up to 100.")

'''

count = 10
givennumber = 2

while count > 0
    for divisor in range(2, givennumber):
        if (givennumver % divisor == 0): break
    else
        count -= 1
        print(givennumber,"is prime number")
        if 