def sort_hyphen_separated(sequence):
    # Split the hyphen-separated sequence into a list of words
    words = sequence.split('-')
    
    # Sort the list of words alphabetically
    sorted_words = sorted(words)
    
    # Join the sorted list back into a hyphen-separated string
    sorted_sequence = '-'.join(sorted_words)
    
    return sorted_sequence

# Example usage:
sample_items = "green-red-yellow-black-white"
result = sort_hyphen_separated(sample_items)

print("Original sequence:", sample_items)
print("Sorted sequence:", result)