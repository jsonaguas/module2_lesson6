first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

def length_check(first_name, last_name):
    if len(first_name) and len(last_name) < 2:
        return "First name and last name must be at least 2 characters long."
    
print(length_check(first_name, last_name))
