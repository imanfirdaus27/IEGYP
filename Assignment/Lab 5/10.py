def stringcompression(a):
    compressed = ""
    count = 1
    print(len(a))
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            count += 1
        else:
            compressed = compressed + a[i-1] + str(count)
            count = 1
    compressed = compressed + a[len(a)-1] + str(count)
    return compressed

a = str(input("Please enter any strings of characters:"))
print(stringcompression(a))

# def stringcompression(a):
#     compressed = ""
#     count = 1
#     print(len(a))
#     for i in range(1, len(a)):
#         if a[i] == a[i-1]:
#             count += 1
#         else:
#             compressed = compressed + a[i-1] + str(count)
#             count = 1
#     compressed = compressed + a[len(a)-1] + str(count)
#     return compressed

# a = str(input("Please enter any strings of characters:"))
# print(stringcompression(a))




# def stringcompression(a):
#     compressed = ""
#     count = 1
#     print(len(a))
#     for i in range(1, len(a)):
#         if a[i] == a[i-1]:
#             count += 1
#         else:
#             compressed += a[i-1] + str(count)
#             count = 1
#     compressed += a[len(a)-1] + str(count) #compressed = compressed + a[len(a)-1] + str(count) 
#     return compressed

# a = (str(input("Please enter any strings of characters:")))
# print(stringcompression(a))