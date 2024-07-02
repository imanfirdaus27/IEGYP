from collections import Counter
import string

def character_frequency(file_path):
    with open(file_path, 'r') as file:
        # Read the content of the file
        text = file.read()
        
    # Filter out non-alphabet characters and convert to lowercase
    filtered_text = [char.lower() for char in text if char.lower() in string.ascii_lowercase]
    
    # Count the frequency of each character
    frequency = Counter(filtered_text)
    
    # Sort the characters alphabetically and print the frequencies
    for char in sorted(frequency):
        print(f"{char}: {frequency[char]}")

# Call the function with the file path
character_frequency('frequencyFile.txt')