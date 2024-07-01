def multiVarFunc():
    # Input from the user
    department_name = input("Enter department name:\n")
    total_students = int(input("Enter the number of total students:\n"))
    total_faculties = int(input("Enter the number of total faculties:\n"))
    
    # Display user inputs
    print("Details:")
    print(f"Department: {department_name}")
    print(f"Total students: {total_students}")
    print(f"Total faculties: {total_faculties}")
    
    # Return multiple values
    return department_name, total_students, total_faculties

# Function call
multiVarFunc()