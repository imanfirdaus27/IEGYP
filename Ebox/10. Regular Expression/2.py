import re

def check_offer_code(s):
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel not in s:
            return "Not Accepted"
    return "Accepted"
    
string = input()
print(check_offer_code(string))