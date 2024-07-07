def is_pangram(sentence):
    
    sentence = sentence.lower()
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    sentence_chars = set(sentence)

    alphabet_set = set(alphabet)

    return alphabet_set.issubset(sentence_chars)

sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print(f"{sentence} is a pangram")
else:
    print(f"{sentence} is not a pangram")