def get_customer_age():  #creates a function; we will call this later to get valid age
    while True: # starts an infinite loop
        user_input = input("Please enter your age: ")
        try:
            age = int(user_input)
            if age <= 0:
                print("Age must be a positive number.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")
def main():
    print("Age Verification")
    message = "Checking customer eligibility..."
    try:
        print(message) # will raise NameError if 'message' is not defined
    except NameError:
        print("A variable was used before being defined (NameError). Fix the code and try again")

    # get a valid age
    age = get_customer_age()

    # check eligibility
    if age >= 18:
        print("You are eligible to purchase this product.")
    else:
        print("You are not eligible to purchase this product.")
main() # call the main function to start the program