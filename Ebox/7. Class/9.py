class College:
    def __str__(self, college_id=None, college_name=None, city=None, state=None, pincode=None,
                contact_number=None, email=None):
        if college_id is not None:
            return f"id : {college_id},Name : {college_name},City : {city},State : {state},Pincode : {pincode}"
        elif contact_number is not None:
            return f"Name : {college_name},Contact Number : {contact_number},Email : {email}"
        else:
            return "Invalid choice"

college = College()


print("1. Enter College address and Display")
print("2. Enter the contact details and Display")
print("3. Exit")
print("\nEnter your choice")
choice = input()

if choice == "1":
    print("Enter the College id")
    college_id = input()
    print("Enter the College name")
    college_name = input()
    print("Enter the City")
    city = input()
    print("Enter the State")
    state = input()
    print("Enter the Pincode")
    pincode = input()

    # Display College address
    print(college.__str__(college_id=college_id, college_name=college_name, city=city,
                        state=state, pincode=pincode))

elif choice == "2":
    print("Enter the name of the College")
    college_name = input()
    print("Enter the contact number")
    contact_number = input()
    print("Enter the email id")
    email = input()

    # Display contact details
    print(college.__str__(college_name=college_name, contact_number=contact_number, email=email))


# hanafi solution
class College:
    def __init__(self, CollegeId, CollegeName, city=None, state=None, pincode=None, contactNumber=None, emailId=None):
        self.CollegeId = CollegeId
        self.CollegeName = CollegeName
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNumber = contactNumber
        self.emailId = emailId
    
    def display_address(self):
        return f"id : {self.CollegeId},Name : {self.CollegeName},City : {self.city},State : {self.state},Pincode : {self.pincode}"
    
    def display_contact_details(self):
        return f"Name : {self.CollegeName},Contact Number : {self.contactNumber},Email : {self.emailId}"

# Main function to handle user input and interactions
def main():
    colleges = []  # List to store College objects
    
    while True:
        print("\n1. Enter College address and Display")
        print("2. Enter the contact details and Display")
        print("3. exit")
        
        choice = input("Enter your choice:\n")
        
        if choice == '1':
            CollegeId = input("Enter the College id\n")
            CollegeName = input("Enter the College name\n")
            city = input("Enter the City\n")
            state = input("Enter the State\n")
            pincode = input("Enter the Pincode\n")
            
            college = College(CollegeId, CollegeName, city, state, pincode)
            colleges.append(college)
            
            print(college.display_address())
        
        elif choice == '2':
            CollegeName = input("Enter the name of the College\n")
            contactNumber = input("Enter the contact number\n")
            emailId = input("Enter the email id\n")
            
            college = College(None, CollegeName, contactNumber=contactNumber, emailId=emailId)
            colleges.append(college)
            
            print(college.display_contact_details())
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()