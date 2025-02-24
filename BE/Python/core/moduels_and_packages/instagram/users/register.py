def user_register():
    """
    This function will register a new user in the system.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        return "Passwords do not match."
    
    # Add user to the system
    return "registration successfully done"
        

def generate_otp():
    import random
    return f"{random.randint(1111, 9999)}"