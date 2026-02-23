
def get_valid_salary_input(prompt): # creates function to get salary
    
    while True: # keeps asking forever until good
        user_input = input(prompt) # shows prompt, waits for user
        try:
            value = float(user_input)
            return value # if successful, send number back
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_percentage():

    while True:
        user_input = input("Enter adjustment percentage (0-100): ")
        try:
            percentage = float(user_input) # convert input to decimal number
            if percentage < 0 or percentage > 100: # check if % is wrong range
                print("Percentage must be between 0 and 100.")
                continue # ask again
            return percentage
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Employee Salary Adjustment Simulator")
    
    # Get current salary
    current_salary = get_valid_salary_input("Enter current salary: $")
    
    # Get adjustment percentage
    adjustment_pct = get_valid_percentage()
    
    # Calculate new salary
    adjustment_amount = current_salary * (adjustment_pct / 100)
    new_salary = current_salary + adjustment_amount
    
    print(f"Current salary: ${current_salary:.2f}")
    print(f"Adjustment: {adjustment_pct}% (+${adjustment_amount:.2f})")
    print(f"New salary: ${new_salary:.2f}")


main()
