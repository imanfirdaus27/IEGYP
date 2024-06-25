# chatgpt sources

# imancode
units = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

teens = {
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

tens = {
    0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 
    5: 'fifty', 6: 'sixty', 7: 'seventy', 
    8: 'eighty', 9: 'ninety'
}


def wordrepresentation(num):

    if num >= 11 and num <=19: 
        words = teens[num]
        return words

    if num >= 100:
       words = units[num // 100] + " hundred "
       num = num % 100
    else: 
        words = ""

    if num >= 20:
        words = words + tens[num // 10] + " "
        num = num % 10
    
    if num >= 1 and num <= 9:
        words = words + units[num]

    return words 
    

num = (int(input("Please enter any number to convert to its word representation:")))
print(wordrepresentation(num))

# chatgpt
# def number_to_words(num):
#     if num == 0:
#         return "zero"
    
#     words = ""
    
#     # Handle hundreds place
#     if num >= 100:
#         words += units[num // 100] + " hundred "
#         num %= 100
    
#     # Handle tens and units place
#     if num >= 20:
#         words += tens[num // 10] + " "
#         num %= 10
#     elif num >= 10:
#         return words + teens[num]
#     else:
#         words += units[num]
    
#     return words.strip()  # Remove trailing space if any (this part is missing masa awal awal buat)

# # Example usage:
# num = int(input("Enter a number: "))
# print(number_to_words(num))

# chatgpt code
# def wordrepresentation(num):
#     units = {
#         0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
#         5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
#     }
    
#     teens = {
#         10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
#         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
#         17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
#     }
    
#     tens = {
#         0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 
#         5: 'fifty', 6: 'sixty', 7: 'seventy', 
#         8: 'eighty', 9: 'ninety'
#     }

#     if num >= 100:
#         words = units[num // 100] + " hundred "
#         num = num % 100
#     else:
#         words = ""

#     if num >= 20:
#         words += tens[num // 10] + " "
#         num = num % 10
#     elif num >= 10:
#         words += teens[num]
#         return words  # Return immediately for teens
    
#     if num >= 1 and num <= 9:
#         words += units[num]

#     return words

# # Example usage:
# num = int(input("Please enter any number to convert to its word representation: "))
# print(wordrepresentation(num))