# Check inventory level and reorder threshold

def get_valid_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("Inventory Checker")

    # get current inventory level
    inventory_level = get_valid_int("What's the current inventory level? ")

    # get minimum reorder threshold
    min_threshold = get_valid_int("What's the minimum reorder threshold? ")

    # check if we need to reorder
    if inventory_level < min_threshold:
        print("Inventory level is below the minimum threshold. Time to reorder!")
    else:
        print("Inventory level is sufficient. No need to reorder.")
    
    # try to calculate % 
    try:
        percentage = (inventory_level / min_threshold) * 100
        print(f"Inventory is {percentage:.2f}% of the threshold.")
    except ZeroDivisionError: #this runs if min threshold is 0 and we try to divide by it
        print("Minimum threshold cannot be zero. Cannot calculate percentage.")
main() # call the main function to start the program