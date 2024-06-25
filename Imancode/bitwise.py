# to represent binary in pyhton 
# we use 0b
# why we use 0b
# so that computer reads one one one zero zero one zero zero one
# instead of reading 111million
# because one zero one is equals to RM5 not RM101

givenbinary = 0b101


filepermission = 0b111101001
print(filepermission) #auto convert binary to decimal and print

# you can use built in function called bin to print it as binary
print(bin(filepermission))
number = 97409
print(bin(number))

# filepermission holds a binary number and I am interested
# only in some bits not all
# for example i am interested only in permission belongs to the group
# which means i am interested in 4, 5, 6 bits only
# Feature Engineering = massage the data to make it data ready to learn #PHDstudent

mask = 0b000111000 # we created on which bits that we are interested
# original            111101001   &
# mask                000111000
# result              000101000 # will not give the answer 5
# the & operators in used for extracting bits we are 
# interested
# let us shift to left 3 times to convert it to 5(the result)
# result 000000101    used     >>3 

print(bin((filepermission & mask) >> 3))
print((filepermission & mask)>>3)


# i want to set 4, 5, 6 bits to 1
# the other bits remain as it is then we use or operator
# original            111010101   |
# mask                000111000
# result              111111101
filepermission = 0b111010101
mask = 0b000111000
print(bin(filepermission |mask))
# using or operators you cannot set the bits to 0

# xor operator = used in encryption
#      or    and   xor
# 1 1   1     1     0
# 1 0   1     0     1
# 0 1   1     0     1
# 0 0   0     0     0

content = 0b10101010 # This can be alphabet J
key  = 0b00111100 # This can be s
# I am going to encrypt J using s
# to decrypt you must know s
encryptedcontent = content ^ key
print (bin(encryptedcontent))

decryptedcontent = encryptedcontent ^ key
print(bin(decryptedcontent))


# 1s compliment = flip the bits from 1 to 0 or 0 to 1
givennumber = 5  # 0101
print(bin(~givennumber)) # 1 110 -6
# get the 1s compliment and add 1 #twos compliment
print(bin(~givennumber + 1))

print(-givennumber) #unary negative
print(+givennumber) #unary positive




