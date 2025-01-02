# Define the input string containing brackets
s = "()[]{}"
# Initialize an empty stack to keep track of opening brackets
stack = []
# Define a mapping of closing brackets to their corresponding opening brackets
mapping = {')': '(', '}': '{', ']': '['}

# Iterate through each character in the string
for char in s:
    # Check if the character is a closing bracket
    if char in mapping:
        # If the stack is not empty and the top of the stack matches the corresponding opening bracket
        if stack and stack[-1] == mapping[char]:
            # Pop the top element from the stack (matching opening bracket found)
            stack.pop()
        else:
            # If the stack is empty or the brackets don't match, the string is invalid
            False
    else:
        # If the character is an opening bracket, push it onto the stack
        stack.append(char)

# Check if the stack is empty (all brackets are matched)
print(True if not stack else False)

