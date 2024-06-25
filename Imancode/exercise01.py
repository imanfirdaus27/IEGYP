# Given number is 76589
# I want you to reverse the number
# Expected output 98567

# givenNumber = 76589
# result = 0
# result = givenNumber % 10 # 9
# givenNumber = givenNumber // 10 #7658
# result = (result*10) + (givenNumber % 10) #98
# givenNumber = givenNumber // 10 #765
# result = (result*10) + (givenNumber % 10) #985
# givenNumber = givenNumber // 10 #76
# result = (result*10) + (givenNumber % 10) #9856
# givenNumber = givenNumber // 10 #7
# result = (result*10) + (givenNumber % 10) #98567

givenNumber = 76589
result = 0
result = givenNumber % 10 # 9
print("Result:", result)
givenNumber = givenNumber // 10 #7658
result = (result*10) + (givenNumber % 10) #98
print("Result:", result)
givenNumber = givenNumber // 10 #765
result = (result*10) + (givenNumber % 10) #985
print("Result:", result)
givenNumber = givenNumber // 10 #76
result = (result*10) + (givenNumber % 10) #9856
print("Result:", result)
givenNumber = givenNumber // 10 #7
result = (result*10) + (givenNumber % 10) #98567
print("Result:", result)


# COI / IRFAN Solution

a0 = 76589
result = 0

a1 = a0 % 10 # 9
a2 = a0 // 10 # 7658
result = result * 10 + a1 # 9

a3 = a2 % 10 # 8
a4 = a2 // 10 # 765
result = result * 10 + a3 # 98

a5 = a4 % 10 # 5
a6 = a4 // 10 # 76
result = result * 10 + a5 # 985

a7 = a6 % 10 # 6
a8 = a6 // 10 # 7
result = result * 10 + a7 # 9856

a9 = a8 % 10 # 7
a10 = a8 // 10 # 0
result = result * 10 + a9 # 98567



# COI Solution with output

# COI / IRFAN Solution

a0 = 76589
result = 0

a1 = a0 % 10 # 9
a2 = a0 // 10 # 7658
result = result * 10 + a1 # 9
print(a1, a2, result)

a3 = a2 % 10 # 8
a4 = a2 // 10 # 765
result = result * 10 + a3 # 98
print(a3, a4, result)

a5 = a4 % 10 # 5
a6 = a4 // 10 # 76
result = result * 10 + a5 # 985
print(a5, a6, result)

a7 = a6 % 10 # 6
a8 = a6 // 10 # 7
result = result * 10 + a7 # 9856
print(a7, a8, result)

a9 = a8 % 10 # 7
a10 = a8 // 10 # 0
result = result * 10 + a9 # 98567
print(a9, a10, result)


# Akmal Solution
x = 76589
 
reversed = (x % 10) * 10000 #90000
reversed = ((x // 10) % 10) * 1000 + reversed #98000
reversed = ((x // 100) % 10) * 100 + reversed #98500
reversed = ((x // 1000) % 10) * 10 + reversed #98560
reversed = (x // 10000) + reversed #98567
print(reversed)