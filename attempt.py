import getpass

def display_menu():
    print("Welcome to the App!")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    return choice

def sign_in(users):
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    if email in users and users[email] == password:
        print("Sign in successful!")
    else:
        print("Invalid email or password.")

def sign_up(users):
    email = input("Enter your email: ")
    if email in users:
        print("Email already exists.")
        return
    full_name = input("Enter your full name: ")
    password = getpass.getpass("Enter your password: ")
    users[email] = password
    print("Sign up successful!")

def main():
    users = {}
    while True:
        choice = display_menu()
        if choice == '1':
            sign_in(users)
        elif choice == '2':
            sign_up(users)
        elif choice == '3':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
