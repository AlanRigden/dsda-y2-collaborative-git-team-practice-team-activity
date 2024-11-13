def calculate_square(number):
    """Calculates the square of a number."""
    return number * number

if __name__ == "__main__":
    user_number = int(input("Enter a number: "))
    result = calculate_square(user_number)
    print(f"The square of {user_number} is {result}")
