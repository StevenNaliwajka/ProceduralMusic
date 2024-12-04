def get_number_int_float(prompt="Enter a number (integer or float): "):
    while True:
        user_input = input(prompt).strip()
        try:
            # Attempt to convert the input to a float
            return float(user_input)
        except ValueError:
            # Handle the case where the input is not a valid number
            print("Invalid input. Please enter a valid number (integer or float).")