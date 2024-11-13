import re

def greet_user(name, age):
    """Greets the user by name and age."""
    if age >= 18:
        print(f"Hello, {name}! Welcome!")
    else:
        print(f"Hi, {name}! How can I help you today?")

if __name__ == "__main__":
    while True:
        user_name = input("Enter your name: ").strip()
        
        if re.fullmatch(r"[A-Z][a-zA-Z ]*", user_name):
            break
        else:
            print("Please enter a valid name (start with a capital letter, no numbers or symbols).")

    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    greet_user(user_name, user_age)
