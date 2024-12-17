def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Database connection and verification
    # Replace this with actual database connection and verification logic
    if username == "admin" and password == "password":
        return "Login successful!"
    else:
        return "Invalid username or password."