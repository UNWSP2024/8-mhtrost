#Micah Trost
#March 17, 2026
#Course Info

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
