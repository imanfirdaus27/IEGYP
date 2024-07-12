# class College:
#     def __init__(self, CollegeId, CollegeName, city=None, state=None, pincode=None, contactNumber=None, emailId=None):
#         self.CollegeId = CollegeId
#         self.CollegeName = CollegeName
#         self.city = city
#         self.state = state
#         self.pincode = pincode
#         self.contactNumber = contactNumber
#         self.emailId = emailId
    
#     def display_address(self):
#         return f"id : {self.CollegeId},Name : {self.CollegeName},City : {self.city},State : {self.state},Pincode : {self.pincode}"
    
#     def display_contact_details(self):
#         return f"Name : {self.CollegeName},Contact Number : {self.contactNumber},Email : {self.emailId}"

# # Main function to handle user input and interactions
#     colleges = []  # List to store College objects
    
# while True:
#     colleges = []

#     print("\n1. Enter College address and Display")
#     print("2. Enter the contact details and Display")
#     print("3. exit")
        
#     choice = input("Enter your choice:\n")
        
#     if choice == '1':
#         CollegeId = input("Enter the College id\n")
#         CollegeName = input("Enter the College name\n")
#         city = input("Enter the City\n")
#         state = input("Enter the State\n")
#         pincode = input("Enter the Pincode\n")
            
#         college = College(CollegeId, CollegeName, city, state, pincode)
#         colleges.append(college)
            
#         print(college.display_address())
        
#     elif choice == '2':
#         CollegeName = input("Enter the name of the College\n")
#         contactNumber = input("Enter the contact number\n")
#         emailId = input("Enter the email id\n")
            
#         college = College(None, CollegeName, contactNumber=contactNumber, emailId=emailId)
#         colleges.append(college)
        
#         print(college.display_contact_details())
        
#     elif choice == '3':
#         break
        
#     else:
#          print("Invalid choice. Please enter 1, 2, or 3.")


# hanafi solution
# class College:
#     def __init__(self, CollegeId, CollegeName, city=None, state=None, pincode=None, contactNumber=None, emailId=None):
#         self.CollegeId = CollegeId
#         self.CollegeName = CollegeName
#         self.city = city
#         self.state = state
#         self.pincode = pincode
#         self.contactNumber = contactNumber
#         self.emailId = emailId
    
#     def display_address(self):
#         return f"id : {self.CollegeId},Name : {self.CollegeName},City : {self.city},State : {self.state},Pincode : {self.pincode}"
    
#     def display_contact_details(self):
#         return f"Name : {self.CollegeName},Contact Number : {self.contactNumber},Email : {self.emailId}"

# Main function to handle user input and interactions
# def main():
#     colleges = []  # List to store College objects
    
#     while True:
#         print("\n1. Enter College address and Display")
#         print("2. Enter the contact details and Display")
#         print("3. exit")
        
#         choice = input("Enter your choice:\n")
        
#         if choice == '1':
#             CollegeId = input("Enter the College id\n")
#             CollegeName = input("Enter the College name\n")
#             city = input("Enter the City\n")
#             state = input("Enter the State\n")
#             pincode = input("Enter the Pincode\n")
            
#             college = College(CollegeId, CollegeName, city, state, pincode)
#             colleges.append(college)
            
#             print(college.display_address())
        
#         elif choice == '2':
#             CollegeName = input("Enter the name of the College\n")
#             contactNumber = input("Enter the contact number\n")
#             emailId = input("Enter the email id\n")
            
#             college = College(None, CollegeName, contactNumber=contactNumber, emailId=emailId)
#             colleges.append(college)
            
#             print(college.display_contact_details())
        
#         elif choice == '3':
#             break
        
#         else:
#             print("Invalid choice. Please enter 1, 2, or 3.")

# if __name__ == "__main__":
#     main()

# class College:
#     def _str_(self, *args):
#         if len(args) == 5:
#             college_id, name, city, state, pincode = args
#             return f"id : {college_id}\nName : {name}\nCity : {city}\nState : {state}\nPincode : {pincode}"
#         elif len(args) == 3:
#             name, contact_number, email_id = args
#             return f"Name : {name}\nContact Number : {contact_number}\nEmail : {email_id}"
#         else:
#             return "Invalid number of arguments"

# def main():
#     while True:
        
#         choice = input("Enter your choice\n")

#         if choice == '1':
#             college_id = input("Enter the College id\n")
#             name = input("Enter the College name\n")
#             city = input("Enter the City\n")
#             state = input("Enter the State\n")
#             pincode = input("Enter the Pincode\n")
#             college = College()
#             print(college._str_(college_id, name, city, state, pincode))
        
#         elif choice == '2':
#             name = input("Enter the name of the College\n")
#             contact_number = input("Enter the contact number\n")
#             email_id = input("Enter the email id\n")
#             college = College()
#             print(college._str_(name, contact_number, email_id))
        
#         elif choice == '3':
#             break
        
#         else:
#             print("Invalid choice. Please enter again.")

# if __name__ == "_main_":
#     print("1. Enter College address and Display")
#     print("2. Enter  the contact details and Display")
#     print("3. exit")
#     main()

class College:
    def __init__(self, college_id,college_name, city = None , state= None,pincode= None, contactNumber= None, emailId= None):
        self.college_id = college_id
        self.college_name = college_name
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNumber = contactNumber
        self.emailId = emailId

    def print_address (self):
        return f"id : {self.college_id}\nName : {self.college_name}\nCity : {self.city}\nState : {self.state}\nPincode : {self.pincode}\n"

    def print_email (self):
        return f"Name : {self.college_name}\nContact Number : {self.contactNumber}\nEmail : {self.emailId}\n"


print("1. Enter College address and Display")
print("2. Enter  the contact details and Display")
print("3. exit")


n = -1
while n !=3:
    n = int(input("Enter your choice\n"))
    if n==1:
        college_id = input("Enter the College id\n")
        college_name = input("Enter the College name\n")
        city = input("Enter the City\n")
        state = input("Enter the State\n")
        pincode = input("Enter the Pincode")
        p1 = College(college_id,college_name, city , state,pincode)
        print(p1.print_address())
    
    elif n==2:
        college_name = input("Enter the name of the College\n")
        contactNumber = input("Enter the contact number\n")
        emailId = input("Enter the email id\n")
        p2 = College(None, college_name,None, None, None, contactNumber, emailId)
        print(p2.print_email())
    else:
        break