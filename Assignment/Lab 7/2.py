def is_isogram(word):
    # Convert the word to lowercase
    lowcaseword = word.lower()
    
    # Set to keep track of seen alphabetic letters
    seen_letters = set()
    
    for letter in lowcaseword:
        # Ignore non-alphabetic characters (spaces and hyphens)
        if letter == ' ' :
            continue
        if letter == '-' :
            continue

        if letter.isalpha():
            # Check if letter is already in seen_letters
            if letter in seen_letters:
                return False
            seen_letters.add(letter)
    
    # If no repeating alphabetic letters found, it's an isogram
    return True

# Get input from user
user_input = input("Please enter your input (String only): ")

# Check if input is an isogram
if is_isogram(user_input):
    print("The string is an isogram")
else:
    print("The string is not an isogram")