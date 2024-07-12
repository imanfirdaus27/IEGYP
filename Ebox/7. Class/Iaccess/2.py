class Student:
    def __init__(self, id, name, department, courseId):
        self.id = id
        self.name = name
        self.department = department
        self.courseId = courseId

    def __str__(self):
        return f"Student:\nId : {self.id}\nName : {self.name}\nDepartment : {self.department}\nCourse Id : {self.courseId}"

class StudentRating:
    def __init__(self, id, review, stars, student):
        self.id = id
        self.review = review
        self.stars = stars
        self.student = student

    def __str__(self):
        return f"{self.student}\nRating ID : {self.id}\nReview : {self.review}\nRating Stars : {self.stars}"

# Reading input from the user
student_id = int(input("Enter the student id\n"))
student_name = input("Enter the student name\n")
student_department = input("Enter the department\n")
student_courseId = int(input("Enter the course id\n"))

rating_id = int(input("Enter the Rating id\n"))
rating_review = input("Enter review\n")
rating_stars = int(input("Enter number of stars\n"))

# Creating Student and StudentRating objects
student = Student(student_id, student_name, student_department, student_courseId)
student_rating = StudentRating(rating_id, rating_review, rating_stars, student)

# Displaying the details
print(student_rating)   