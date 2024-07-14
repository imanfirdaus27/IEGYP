class ParenthesesChecker:
    def __init__(self):
        self.opening_brackets = {'(', '[', '{'}
        self.closing_brackets = {')': '(', ']': '[', '}': '{'}
    
    def is_valid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack or stack[-1] != self.closing_brackets[char]:
                    return False
                stack.pop()
        
        # After iterating through all characters, stack should be empty for valid parentheses
        return len(stack) == 0

if __name__ == "__main__":
    checker = ParenthesesChecker()
    
    # Prompt user for input
    while True:
        input_string = input("Enter a string with parentheses: ")
        
        if input_string.lower() == 'quit':
            break
        
        # Check validity
        if checker.is_valid(input_string):
            print(f"'{input_string}' -> Valid")
        else:
            print(f"'{input_string}' -> Invalid")
