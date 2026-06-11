from services.school_system import SchoolSystem

def main():
    school = SchoolSystem()
    school.load_data()

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Register Student to Course")
        print("7. View Students in a Course")
        print("8. View Courses for a Student")
        print("9. Save Data")
        print("10. Load Data")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            school.add_student()
        elif choice == "2":
            school.view_students()
        elif choice == "3":
            school.search_student()
        elif choice == "4":
            school.add_course()
        elif choice == "5":
            school.view_courses()
        elif choice == "6":
            school.register_student()
        elif choice == "7":
            school.view_students_in_course()
        elif choice == "8":
            school.view_courses_for_student()
        elif choice == "9":
            school.save_data()
        elif choice == "10":
            school.load_data()
            print("Data loaded.")
        elif choice == "0":
            school.save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
