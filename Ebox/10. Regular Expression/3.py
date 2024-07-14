import re
def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^\+91-\d{10}$')
    if pattern.match(phone_number):
        return "Not a Spam Call"
    else:
        return "Spam Call"
    
num = input()
print(is_valid_phone_number(num))