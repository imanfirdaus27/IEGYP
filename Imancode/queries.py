# check ewhether the given number
givenNumber = 11
divisors = range(2, givenNumber)

if(len([mynumber for mynumber in divisors if (givenNumber % mynumber == 0)])==0):#check this in python tutor
    print(givenNumber, "is a prime number")
else:
    print(givenNumber, "is not a prime number")

[givenNumber % mynumber == 0 for mynumber in divisors]




if any([givenNumber % mynumber == 0 for mynumber in divisors]): # check this in python tutor
    print(givenNumber, "is not a prime number")
else:
    print(givenNumber, "is a prime number")

# try this exercise
# check whether the given number is Prime or not
# check whether the input is prime or not
# generate first 10 prime numbers
# generate prime numbers between 10 -100

         
