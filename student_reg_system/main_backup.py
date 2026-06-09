import os

# ==========================
#         CLASSES
# ==========================

class User:
    def __init__(self, reg_number, name, email):
        self.reg_number = reg_number
        self.name = name
        self.email = email

class Student(User):
    def __init__(self, reg_number, name, email):
        super().__init__(reg_number, name, email)
        self.courses = []

class Teacher(User):
    def __init__(self, reg_number, name, email, department):
        super().__init__(reg_number, name, email)
        self.department = department

class Course:
    def __init__(self, course_id, course_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity
        self.students_enrolled = []


# ==========================
#     GLOBAL VARIABLES
# ==========================
students_list = []
courses_list = []

def save_data():
    file = open("data.txt", "w")
    
    file.write("---STUDENTS---\n")
    for s in students_list:
        file.write(f"{s.reg_number},{s.name},{s.email}\n")
        # Save their courses too!
        if len(s.courses) > 0:
            file.write(f"COURSES:{','.join(s.courses)}\n")
        else:
            file.write("COURSES:None\n")
            
    file.write("---COURSES---\n")
    for c in courses_list:
        file.write(f"{c.course_id},{c.course_name},{c.capacity}\n")
        if len(c.students_enrolled) > 0:
            file.write(f"ENROLLED:{','.join(c.students_enrolled)}\n")
        else:
            file.write("ENROLLED:None\n")
            
    file.close()
    print("Data saved successfully to data.txt!")

def load_data():
    try:
        file = open("data.txt", "r")
        lines = file.readlines()
        file.close()
        
        students_list.clear()
        courses_list.clear()
        
        reading_mode = ""
        last_student = None
        last_course = None
        
        for line in lines:
            line = line.strip() 
            
            if line == "---STUDENTS---":
                reading_mode = "students"
            elif line == "---COURSES---":
                reading_mode = "courses"
            else:
                if reading_mode == "students":
                    if line.startswith("COURSES:"):
                        course_data = line.replace("COURSES:", "")
                        if course_data != "None" and last_student != None:
                            last_student.courses = course_data.split(",")
                    else:
                        parts = line.split(",")
                        if len(parts) == 3:
                            last_student = Student(parts[0], parts[1], parts[2])
                            students_list.append(last_student)
                            
                elif reading_mode == "courses":
                    if line.startswith("ENROLLED:"):
                        enrolled_data = line.replace("ENROLLED:", "")
                        if enrolled_data != "None" and last_course != None:
                            last_course.students_enrolled = enrolled_data.split(",")
                    else:
                        parts = line.split(",")
                        if len(parts) == 3:
                            last_course = Course(parts[0], parts[1], int(parts[2]))
                            courses_list.append(last_course)
    except FileNotFoundError:
        pass # It's okay if the file doesn't exist yet

# Load data automatically when the program starts
load_data()


# ==========================
#        MAIN LOOP
# ==========================
while True:
    print("\n      === Noka Schools Reg System ===")
    print("1. List Students")
    print("2. Add Student")
    print("3. List Courses")
    print("4. Course Management")
    print("5. Register a student for a course")
    print("7. List students & courses")
    print("9. Save and exit")
    print("0. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        if len(students_list) == 0:
            print("No students found.")
        else:
            print(f"{'Name':<20} | {'Reg Number':<12} | {'Enrolled Courses'}")
            print("-" * 60)
            for s in students_list:
                if len(s.courses) > 0:
                    courses_str = ", ".join(s.courses)
                else:
                    courses_str = "None"
                print(f"{s.name:<20} | {s.reg_number:<12} | {courses_str}")
                
    elif choice == '2':
        s_name = input("Enter Student Name: ")
        s_email = input("Enter Student Email: ")
        s_reg = input("Enter Reg Number: ")
        
        new_student = Student(s_reg, s_name, s_email)
        students_list.append(new_student)
        print("Student added successfully!")
        
        register_now = input("\nWould you like to register this student for a course right now? (y/n): ")
        if register_now.lower() == 'y':
            if len(courses_list) == 0:
                print("There are no courses available yet. Please add a course from the main menu first.")
            else:
                print("\nAvailable Courses:")
                for index, c in enumerate(courses_list):
                    print(f"{index + 1}. {c.course_id} - {c.course_name}")
                    
                course_choice = input("Enter the number of the course to register: ")
                try:
                    c_index = int(course_choice) - 1
                    
                    if c_index >= 0 and c_index < len(courses_list):
                        selected_course = courses_list[c_index]
                        
                        if len(selected_course.students_enrolled) >= selected_course.capacity:
                            print("Error: Course is full.")
                        elif selected_course.course_id in new_student.courses:
                            print("Error: Student is already in this course.")
                        else:
                            new_student.courses.append(selected_course.course_id)
                            selected_course.students_enrolled.append(new_student.reg_number)
                            print(f"Success! {new_student.name} is now registered for {selected_course.course_name}.")
                    else:
                        print("Error: Invalid course number selected.")
                except ValueError:
                    print("Error: Please enter a valid number.")

    elif choice == '3':
        if len(courses_list) == 0:
            print("No courses found.")
        else:
            print(f"{'Course ID':<15} | {'Course Name':<20} | {'Capacity'}")
            print("-" * 55)
            for c in courses_list:
                print(f"{c.course_id:<15} | {c.course_name:<20} | {len(c.students_enrolled)}/{c.capacity}")
                
    elif choice == '4':
        print("\n--- Course Management ---")
        print("1. Create new course")
        print("2. Edit existing course")
        sub_choice = input("Enter your choice (1 or 2): ")
        
        if sub_choice == '1':
            c_id = input("Enter Course ID: ")
            c_name = input("Enter Course Name: ")
            c_cap = input("Enter Capacity (number): ")
            
            try:
                capacity = int(c_cap)
                new_course = Course(c_id, c_name, capacity)
                courses_list.append(new_course)
                print("Course added successfully!")
            except ValueError:
                print("Error: Capacity must be a number!")
                
        elif sub_choice == '2':
            if len(courses_list) == 0:
                print("No courses available to edit. Create one first!")
            else:
                print("\nWhich course would you like to edit?")
                for index, c in enumerate(courses_list):
                    print(f"{index + 1}. {c.course_id} - {c.course_name}")
                    
                course_choice = input("Enter the number of the course: ")
                try:
                    c_index = int(course_choice) - 1
                    if 0 <= c_index < len(courses_list):
                        selected_course = courses_list[c_index]
                        print(f"\nEditing: {selected_course.course_id} - {selected_course.course_name}")
                        
                        new_id = input("Enter new Course ID: ")
                        new_name = input("Enter new Course Name: ")
                        new_cap = input("Enter new Capacity (number): ")
                        
                        selected_course.course_id = new_id
                        selected_course.course_name = new_name
                        selected_course.capacity = int(new_cap)
                        
                        print("Course updated successfully!")
                    else:
                        print("Error: Invalid course number.")
                except ValueError:
                    print("Error: Capacity and Course choice must be valid numbers!")
        else:
            print("Invalid choice. Returning to main menu.")
            
    elif choice == '5':
        if len(students_list) == 0:
            print("No students available. Add one first!")
        elif len(courses_list) == 0:
            print("No courses available. Add one first!")
        else:
            print("\n--- Available Students ---")
            for index, s in enumerate(students_list):
                print(f"{index + 1}. {s.name} (Reg: {s.reg_number})")
                
            s_input = input("Enter the number from the list (or type exact Reg Number): ")
            
            found_student = None
            # Try to find by exact Reg Number first
            for s in students_list:
                if s.reg_number == s_input:
                    found_student = s
                    break
                    
            # If not found by Reg Number, try to use it as a list number
            if found_student == None:
                try:
                    s_index = int(s_input) - 1
                    if 0 <= s_index < len(students_list):
                        found_student = students_list[s_index]
                except ValueError:
                    pass # Ignore if it wasn't a number
                    
            if found_student == None:
                print("Error: Student not found.")
            else:
                print("\n--- Available Courses ---")
                for index, c in enumerate(courses_list):
                    print(f"{index + 1}. {c.course_name} (ID: {c.course_id})")
                    
                c_input = input("Enter the number from the list (or type exact Course ID): ")
                
                found_course = None
                # Try exact Course ID first
                for c in courses_list:
                    if c.course_id == c_input:
                        found_course = c
                        break
                        
                # Try as list number
                if found_course == None:
                    try:
                        c_index = int(c_input) - 1
                        if 0 <= c_index < len(courses_list):
                            found_course = courses_list[c_index]
                    except ValueError:
                        pass
                        
                if found_course == None:
                    print("Error: Course not found.")
                else:
                    if len(found_course.students_enrolled) >= found_course.capacity:
                        print("Error: Course is full.")
                    elif found_course.course_id in found_student.courses:
                        print("Error: Student is already in this course.")
                    else:
                        found_student.courses.append(found_course.course_id)
                        found_course.students_enrolled.append(found_student.reg_number)
                        print(f"Success! {found_student.name} registered for {found_course.course_name}.")
                
    elif choice == '7':
        print("\n--- ALL STUDENTS ---")
        if len(students_list) == 0:
            print("No students found.")
        else:
            print(f"{'Name':<20} | {'Reg Number':<12} | {'Enrolled Courses'}")
            print("-" * 60)
            for s in students_list:
                courses_str = ", ".join(s.courses) if len(s.courses) > 0 else "None"
                print(f"{s.name:<20} | {s.reg_number:<12} | {courses_str}")
                
        print("\n--- ALL COURSES ---")
        if len(courses_list) == 0:
            print("No courses found.")
        else:
            print(f"{'Course ID':<15} | {'Course Name':<20} | {'Capacity'}")
            print("-" * 55)
            for c in courses_list:
                print(f"{c.course_id:<15} | {c.course_name:<20} | {len(c.students_enrolled)}/{c.capacity}")
                
    elif choice == '9':
        save_data()
        print("Goodbye!")
        break
        
    elif choice == '0':
        print("Exiting without saving. Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")
