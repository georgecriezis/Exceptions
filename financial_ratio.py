

def get_valid_financial_input(prompt):
   
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            pass  #  ignore bad input and ask again


def main():
    print("Financial Ratio Calculator")
    
    while True:  # loop until everything works
        # Get profit and revenue
        profit = get_valid_financial_input("Enter profit amount: $")
        revenue = get_valid_financial_input("Enter revenue amount: $")
        
        # Try to calculate ratio with try-except-else
        try:
            ratio = profit / revenue  # might cause ZeroDivisionError
        except ZeroDivisionError:
            pass  #  ignore zero revenue and ask again
        except ValueError:
            pass  #  ignore other errors and ask again
        else:
            # This only runs if no exceptions happened
            percentage = ratio * 100
            print(f"Profit margin: {percentage:.2f}%")
            break  


main()
