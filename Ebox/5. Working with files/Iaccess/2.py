# 4  # Input: number of persons
# nisha  # Input: person's name
# 30000  # Input: person's salary
# karthikeyan  # Input: next person's name
# 40000  # Input: next person's salary
# krishna  # Input: next person's name
# 30000  # Input: next person's salary
# shakthi  # Input: next person's name
# 35000  # Input: next person's salary

def write_salary_data_to_file(file_path):
    # Read number of persons from input
    n = int(input().strip())
    
    with open(file_path, 'w') as file:
        # Loop to read each person's name and salary
        for _ in range(n):
            name = input().strip()
            salary = input().strip()
            file.write(f"{name},{salary}\n")
    
    # Print the contents of the file
    print(f"Contents of {file_path}:")
    with open(file_path, 'r') as file:
        print(file.read())

# Call the function to execute the process
write_salary_data_to_file('salaryData.csv')