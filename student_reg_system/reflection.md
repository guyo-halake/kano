Project Reflection

Q: What was the hardest part of this project?
A: The hardest part for me was learning how to search my lists. When someone typed a Registration Number, I had to figure out how to loop through the whole students_list to find the one specific object that matched that number.

Q: Which classes did you create and why?
A: I made four classes. First, I made a base User class. Then, I made Student and Teacher classes that inherit from User to prove I know how inheritance works. Lastly, I made a Course class to keep track of course names, capacities, and the students enrolled in them.

Q: How does your registration logic prevent duplicate registrations?
A: When a student tries to join, I look at the list of courses saved inside that Student's object. I use an 'if' statement to check if the course ID is already inside their list. If it is, the program prints an error and stops them.

Q: How does your system check if a course is full?
A: I use the len() function to count how many students are currently inside the course's enrolled list. If that number is equal to or bigger than the capacity limit, the program says the course is full and stops them.

Q: What bugs did you face and how did you fix them?
A: One bug was that if someone typed a word like "hello" instead of a number for the course capacity, my program crashed. I fixed it by wrapping that code in a try/except ValueError block so it prints an error message instead of breaking. Another bug was in my menu selection. If I had 3 courses, but the user typed number 5, it crashed. I fixed this by writing an if statement to make sure the number they typed was actually within the length of the list.

Q: Which part of the code would improve if you had more time?
A: If I had more time, I would break my big menu loop into smaller functions. Right now my main.py is getting very long and it would be easier to read if I split it up. I would also add a way to delete a student from the system completely.
