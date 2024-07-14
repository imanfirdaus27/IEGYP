# List of math problems
test_problems = [
    "What is 5?",
    "What is 5 plus 13?",
    "What is 7 minus 5?",
    "What is 6 multiplied by 4?",
    "What is 25 divided by 5?",
    "What is 5 plus 13 plus 6?",
    "What is 3 plus 2 multiplied by 3?"
]

# Iterate through each problem
for problem in test_problems:
    # Clean up the problem statement
    cleaned_problem = problem.lower().strip()
    if cleaned_problem.startswith("what is ") and cleaned_problem.endswith("?"):
        cleaned_problem = cleaned_problem[8:-1]

    # Replace verbal operations with mathematical operators
    cleaned_problem = cleaned_problem.replace("plus", "+")
    cleaned_problem = cleaned_problem.replace("minus", "-")
    cleaned_problem = cleaned_problem.replace("multiplied by", "*")
    cleaned_problem = cleaned_problem.replace("divided by", "/")
    
    # Evaluate the expression using eval safely
    try:
        result = eval(cleaned_problem)
        print(f"{problem} -> {int(result)}")
    except Exception as e:
        print(f"{problem} -> Error: {str(e)}")
