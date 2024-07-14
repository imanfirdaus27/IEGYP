
import re

def find_password(hint):
    numbers = re.findall(r'\d+', hint)
    if not numbers:
        return "No Password"
    return max(numbers, key=int)

hint = input()
print(find_password(hint))