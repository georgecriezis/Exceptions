# simulate entering sales data for a retail business
# Prompt user (e.g. store manager) for the number of units sold and the price per unit
# use a loop to reprompt if invalid inputs are provided ( non numeric numbers)

# define this outside of main so everyone can use it
def get_valid_number(prompt, number_type):
        while True:
            user_input = input(prompt) # shows the user the prompt text
            try:
                value = number_type(user_input)  # tries to convert the user_input string into a number
                return value                    
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    print("Sales Data Entry")

    # Get valid integer for units sold
    units_sold = get_valid_number("What's the number of units sold? ", int)

                # Get valid float for price per unit
    price_per_unit = get_valid_number("What's the price per unit? ", float)

                #Calculate total sales
    total_sales = units_sold * price_per_unit

    print(f"Total sales is ${total_sales:.2f}")

main() # call the main function to start the program