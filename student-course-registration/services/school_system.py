import json
from models.student import Student
from models.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []
        
    def add_student(self):
        print("\n--- Add New Student ---")
        if len(self.students) > 0:
            print("Existing Student IDs:")
            for student in self.students:
                print("- " + student.student_id + " (" + student.name + ")")
            print("-----------------------")
            
        student_id = input("Enter new Student ID: ")
        if student_id == "":
            print("Error: Student ID cannot be empty.")
            return
            
        # check if student id is already used
        for student in self.students:
            if student.student_id == student_id:
                print("Error: Student ID already exists.")
                return
                
        name = input("Name: ")
        if name == "":
            print("Error: Name cannot be empty.")
            return
            
        email = input("Email: ")
        if "@" not in email:
            print("Error: Email must contain @.")
            return
            
        phone_number = input("Phone: ")
        if phone_number == "":
            print("Error: Phone number cannot be empty.")
            return
            
        new_student = Student(student_id, name, email, phone_number)
        self.students.append(new_student)
        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return
            
        print("\n--- All Students ---")
        for student in self.students:
            print("Student ID: " + student.student_id)
            print("Name: " + student.name)
            print("Email: " + student.email)
            print("Phone: " + student.phone_number)
            print("-------------------------")

    def search_student(self):
        search_term = input("Enter Student ID or Name to search: ").lower()
        found = False
        for student in self.students:
            if search_term in student.student_id.lower() or search_term in student.name.lower():
                print("\n--- Student Found ---")
                print("Student ID: " + student.student_id)
                print("Name: " + student.name)
                print("Email: " + student.email)
                print("Phone: " + student.phone_number)
                found = True
        if found == False:
            print("Student not found.")

    def add_course(self):
        print("\n--- Add New Course ---")
        if len(self.courses) > 0:
            print("Existing Course IDs:")
            for course in self.courses:
                print("- " + course.course_id + " (" + course.course_name + ")")
            print("----------------------")
            
        course_id = input("Enter new Course ID: ")
        if course_id == "":
            print("Error: Course ID cannot be empty.")
            return
            
        # check if course id is already used
        for course in self.courses:
            if course.course_id == course_id:
                print("Error: Course ID already exists.")
                return
                
        course_name = input("Course Name: ")
        if course_name == "":
            print("Error: Course name cannot be empty.")
            return
            
        trainer_name = input("Trainer Name: ")
        
        capacity_str = input("Capacity: ")
        if capacity_str.isdigit() == False:
            print("Error: Capacity must be a number.")
            return
            
        capacity = int(capacity_str)
        if capacity <= 0:
            print("Error: Capacity must be greater than 0.")
            return
            
        new_course = Course(course_id, course_name, trainer_name, capacity)
        self.courses.append(new_course)
        print("Course added successfully!")

    def view_courses(self):
        if len(self.courses) == 0:
            print("No courses found.")
            return
            
        print("\n--- All Courses ---")
        for course in self.courses:
            print("Course ID: " + course.course_id)
            print("Course Name: " + course.course_name)
            print("Trainer: " + course.trainer_name)
            print("Capacity: " + str(course.capacity) + " students")
            print("-------------------------")

    def register_student(self):
        if len(self.students) == 0:
            print("No students available. Please add a student first.")
            return
            
        if len(self.courses) == 0:
            print("No courses available. Please add a course first.")
            return
            
        print("\n--- Select a Student ---")
        # List all students with numbers
        index = 1
        for student in self.students:
            print(str(index) + ". " + student.name + " (" + student.student_id + ")")
            index = index + 1
            
        choice_str = input("Enter the number of the student: ")
        if choice_str.isdigit() == False:
            print("Error: Please enter a valid number.")
            return
            
        choice = int(choice_str)
        if choice < 1 or choice > len(self.students):
            print("Error: Invalid student selection.")
            return
            
        found_student = self.students[choice - 1]
        
        print("\n--- Select a Course ---")
        # List all courses with capacities
        index = 1
        for course in self.courses:
            # calculate current enrollment
            current_students_count = 0
            for reg in self.registrations:
                if reg["course_id"] == course.course_id:
                    current_students_count = current_students_count + 1
                    
            status = str(current_students_count) + "/" + str(course.capacity)
            if current_students_count >= course.capacity:
                status = status + " (Course enrollment is full)"
                
            print(str(index) + ". " + course.course_name + " (" + course.course_id + ") - " + status)
            index = index + 1
            
        c_choice_str = input("Enter the number of the course: ")
        if c_choice_str.isdigit() == False:
            print("Error: Please enter a valid number.")
            return
            
        c_choice = int(c_choice_str)
        if c_choice < 1 or c_choice > len(self.courses):
            print("Error: Invalid course selection.")
            return
            
        found_course = self.courses[c_choice - 1]
        
        # check if already registered
        for reg in self.registrations:
            if reg["student_id"] == found_student.student_id and reg["course_id"] == found_course.course_id:
                print("Error: " + found_student.name + " is already registered for this course.")
                return
                
        # check if course is full
        current_students_count = 0
        for reg in self.registrations:
            if reg["course_id"] == found_course.course_id:
                current_students_count = current_students_count + 1
                
        if current_students_count >= found_course.capacity:
            print("Registration failed. This course is already full.")
            return
            
        # register student
        new_registration = {
            "student_id": found_student.student_id,
            "course_id": found_course.course_id
        }
        self.registrations.append(new_registration)
        print("Student " + found_student.name + " successfully registered for " + found_course.course_name + ".")

    def view_students_in_course(self):
        if len(self.courses) == 0:
            print("No courses found.")
            return
            
        print("\n--- Select a Course ---")
        index = 1
        for course in self.courses:
            print(str(index) + ". " + course.course_name + " (" + course.course_id + ")")
            index = index + 1
            
        c_choice_str = input("Enter the number of the course: ")
        if c_choice_str.isdigit() == False:
            print("Error: Please enter a valid number.")
            return
            
        c_choice = int(c_choice_str)
        if c_choice < 1 or c_choice > len(self.courses):
            print("Error: Invalid course selection.")
            return
            
        found_course = self.courses[c_choice - 1]
        course_id = found_course.course_id
                
        if found_course == None:
            print("Error: Course not found.")
            return
            
        print("\n--- Students in " + found_course.course_name + " ---")
        count = 0
        for reg in self.registrations:
            if reg["course_id"] == course_id:
                # get student name
                for student in self.students:
                    if student.student_id == reg["student_id"]:
                        print("- " + student.name + " (" + student.student_id + ")")
                        count = count + 1
        if count == 0:
            print("No students are registered for this course yet.")

    def view_courses_for_student(self):
        if len(self.students) == 0:
            print("No students found.")
            return
            
        print("\n--- Select a Student ---")
        index = 1
        for student in self.students:
            print(str(index) + ". " + student.name + " (" + student.student_id + ")")
            index = index + 1
            
        choice_str = input("Enter the number of the student: ")
        if choice_str.isdigit() == False:
            print("Error: Please enter a valid number.")
            return
            
        choice = int(choice_str)
        if choice < 1 or choice > len(self.students):
            print("Error: Invalid student selection.")
            return
            
        found_student = self.students[choice - 1]
        student_id = found_student.student_id
                
        if found_student == None:
            print("Error: Student not found.")
            return
            
        print("\n--- Courses for " + found_student.name + " ---")
        count = 0
        for reg in self.registrations:
            if reg["student_id"] == student_id:
                # get course name
                for course in self.courses:
                    if course.course_id == reg["course_id"]:
                        print("- " + course.course_name + " (" + course.course_id + ")")
                        count = count + 1
        if count == 0:
            print("Student is not registered in any courses yet.")

    def save_data(self):
        # save students
        students_data = []
        for student in self.students:
            student_dict = {
                "student_id": student.student_id,
                "name": student.name,
                "email": student.email,
                "phone_number": student.phone_number
            }
            students_data.append(student_dict)
            
        file1 = open("data/students.json", "w")
        json.dump(students_data, file1)
        file1.close()
        
        # save courses
        courses_data = []
        for course in self.courses:
            course_dict = {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "trainer_name": course.trainer_name,
                "capacity": course.capacity
            }
            courses_data.append(course_dict)
            
        file2 = open("data/courses.json", "w")
        json.dump(courses_data, file2)
        file2.close()
        
        # save registrations
        file3 = open("data/registrations.json", "w")
        json.dump(self.registrations, file3)
        file3.close()
        
        print("Data saved successfully.")

    def load_data(self):
        # load students
        try:
            file1 = open("data/students.json", "r")
            students_data = json.load(file1)
            file1.close()
            
            self.students = []
            for item in students_data:
                student = Student(item["student_id"], item["name"], item["email"], item["phone_number"])
                self.students.append(student)
        except Exception:
            pass # ignore if file not found
            
        # load courses
        try:
            file2 = open("data/courses.json", "r")
            courses_data = json.load(file2)
            file2.close()
            
            self.courses = []
            for item in courses_data:
                course = Course(item["course_id"], item["course_name"], item["trainer_name"], item["capacity"])
                self.courses.append(course)
        except Exception:
            pass
            
        # load registrations
        try:
            file3 = open("data/registrations.json", "r")
            self.registrations = json.load(file3)
            file3.close()
        except Exception:
            pass
