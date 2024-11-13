import Calculating_squares

def greet_user(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)
    user_number = int(input("Enter a number: "))
    result = Calculating_squares.calculate_square(user_number)
    print(f"The square of {user_number} is {result}")

