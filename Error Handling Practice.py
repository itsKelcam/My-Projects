def divide_nums():
    try:
        # Get user input and convert to float
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        
        # Perform division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result:.2f}")
    
    except ValueError:
        print("That isn't a valid number. Please enter numeric values.")
    
    except ZeroDivisionError:
        print("You can't divide by zero. Try again with a non-zero divisor.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
divide_nums()
