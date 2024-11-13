def save_to_log(name, age, user_number, square):
    """Saves user data to a log file."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"{name} (age {age}): Square of {user_number} is {square}.\n")

def greet_user(name, age):
    """Greets the user by name and age."""
    if age >= 18:
        print(f"Hello, {name}! Welcome!")
    else:
        print(f"Hi, {name}! How can I help you today?")

def calculate_square(number):
    """Calculates the square of a number."""
    return number * number

if __name__ == "__main__":
    # this could be improved by importing their functions not just copying
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    greet_user(user_name, user_age)
    user_number = int(input("Enter a number: "))
    result = calculate_square(user_number)
    print(f"The square of {user_number} is {result}")
    save_to_log(user_name, user_age, user_number, result)
