# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    course_dict = {}
    while True:
        course_id = input("Enter a course ID (or 'done' to finish): ")
        if course_id.lower() == 'done':
            break
        course_name = input("Enter the course name: ")
        course_dict[course_id] = course_name

    subject = input("Enter a subject to search for (e.g., 'COS'): ")
    print(f"Courses in the subject '{subject}':")
    for course_id, course_name in course_dict.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")

course_info()