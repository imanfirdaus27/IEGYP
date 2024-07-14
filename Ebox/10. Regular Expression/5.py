def validate_pan_number(pan_number):
    # Check length of PAN number
    if len(pan_number) != 10:
        return "Invalid PAN Number"
    
    # Check first 5 characters are letters
    if not pan_number[:5].isalpha():
        return "Invalid PAN Number"
    
    # Check next 4 characters are numbers
    if not pan_number[5:9].isdigit():
        return "Invalid PAN Number"
    
    # Check last character is a letter
    if not pan_number[9].isalpha():
        return "Invalid PAN Number"
    
    # Check all characters in PAN number are uppercase
    if not pan_number.isupper():
        return "Invalid PAN Number"
    
    return "Valid PAN Number"

def main():
    pan_number = input()
    print(validate_pan_number(pan_number))

if __name__ == "__main__":
    main()