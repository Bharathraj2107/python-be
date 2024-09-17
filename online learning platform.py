# #onlinre learning platform
# class course:
#     "we provide courses"
# class student(course):
#     def enroll_in_course(self):
#         name=input("enter your name")
#         course=input("enter the course name you want to enroll")
#         print(f"{name} has enrolled in {course}")
#     def complete_lesson(self):
#         name=input("enter your name")
#         lessons=input("enter the number of lessons completed")
#         print(f"{name} has completed these lessons{lessons}")
# print(course.__doc__)#it is used to print what is inside the class written in double quotes
# st1=student()
# st1.enroll_in_course()
# st1.complete_lesson()

#Hospital patient management

class patient:
    def schedule_appointment(self):
        name = input("enter the name of the patient")
        Time = input("Enter the time needed to schedule the appointment")
        print(f"{name} has scheduled an appointment at {Time}")
class Doctor(patient):
    def display_info(self):
        super().schedule_appointment()#can we get only print statement
        location=input("enter the location where you reside")
        reason=input("enter the reason for vist")
        print(f"resides in {location} and the reason for visit is {reason}")
p=patient()
p.schedule_appointment()
d=Doctor()
d.display_info()

        


