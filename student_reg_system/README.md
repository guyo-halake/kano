Noka Schools Reg System

How to run it:
First, open your terminal or command prompt. Navigate into the student_reg_system folder. 
- If you are on Linux or Mac, run it by typing: python3 main.py
- If you are on Windows, run it by typing: python main.py

What the project does:
This is a command line tool I built to register students into different school courses. It lets you create courses, add students, and easily assign students to those courses without making mistakes.

Features I added:
- Main Menu: A menu that stays open until you press 0 to exit, so you don't have to restart the program every time.
- Smart Registration: When you add a new student, the program immediately asks if you want to register them for a course to save time.
- Duplicate Checker: The program checks the student's list of courses. If they are already in the course, it prints an error and stops them from joining twice.
- Capacity Limits: The program counts how many students are in a course. If the course is full, it blocks any new students from joining.
- Data Saving: The program saves all the information into a data.txt file. When you open the program again, it reads the file so your students and courses are still there.

Classes I used:
- User class: This is my base class. It holds the basic details like name and email.
- Student class: This class inherits from the User class. I added a blank list inside it to hold the courses the student joins.
- Teacher class: This also inherits from the User class, but it holds a department name instead.
- Course class: This class holds the course details, like its name, how many students fit inside, and a list of who is currently enrolled.

Challenge I faced:
One big challenge for me was figuring out how to search through my lists. When a user typed in a Student's Registration Number, I didn't know how to find that exact student. I had to learn how to write a 'for loop' to go through every single student in the list, check if their registration number matched what the user typed, and then save that student to a variable so I could use it.
