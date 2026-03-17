#Micah Trost
#March 17, 2026
#Initials Generator

def initials_generator(persons_name):

    persons_initials = ""
    split_name = persons_name.split()
    for name in split_name:
        persons_initials += name[0].upper() + ". "

    return persons_initials.strip()

if __name__=="__main__":
    persons_name = input('Enter the users first, middle, and last name: ')

    initials = initials_generator(persons_name)

    print("Your initials are:", initials)
