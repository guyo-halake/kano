# Student Course Registration System

This is a simple command-line Python application that helps a small training school manage students, courses, and student registrations. 

## How to run the project
1. Open your terminal.
2. Go to the project folder (`student-course-registration`).
3. Run the following command:
   `python main.py` or `python3 main.py`

## Features implemented
- Add new students and view them.
- Search for a student by ID or name.
- Add new courses and view them.
- Register students to courses.
- Prevent duplicate students and courses.
- Prevent registering if the course is full.
- Save data to JSON files and load data from them.

## Classes used
- **Person**: A base class with basic details (name, email, phone).
- **Student**: Inherits from Person and adds a student ID.
- **Course**: Stores course details like ID, name, trainer, and capacity.
- **SchoolSystem**: Handles all the logic, lists, and file saving/loading.

## Challenges faced
- Managing data across different files was tricky but rewarding.
- Making sure the program does not crash when the user types wrong information.
