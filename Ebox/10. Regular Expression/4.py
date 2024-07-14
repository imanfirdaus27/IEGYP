def encrypt(s1, s2):
    encrypted = []
    len1, len2 = len(s1), len(s2)
    
    min_len = min(len1, len2)
    
    # Interleave the characters as described
    for i in range(min_len):
        encrypted.append(s1[i])
        encrypted.append(s2[-(i+1)])
    
    # If any characters are left in the longer string, add them to the result
    if len1 > len2:
        encrypted.extend(s1[min_len:])
    elif len2 > len1:
        encrypted.extend(s2[:len2 - min_len][::-1])
    
    return ''.join(encrypted)

# Sample Input
s1 = input()
s2 = input()

# Encrypt and print the result
print(encrypt(s1, s2))