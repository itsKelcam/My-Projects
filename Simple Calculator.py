while True:
    number_one = input("Please enter a number:")
    sign = input("Please enter what you want to do with the number:")
    number_two = input("Please enter another number:")
    
    while True:
        if not number_one.isdigit():
            number_one = input("Please enter a valid number:")
        elif not number_two.isdigit():
            number_two = input("Please enter a valid number:")
        else:
            break
    
    if sign in ["+", "add", "Add", "ADD", "plus", "Plus", "PLUS"]:
        result = int(number_one) + int(number_two)
    elif sign in ["-", "subtract", "Subtract", "SUBTRACT", "minus", "Minus", "MINUS"]:
        result = int(number_one) - int(number_two)
    elif sign in ["*", "multiply", "Multiply", "MULTIPLY", "times", "Times", "TIMES"]:
        result = int(number_one) * int(number_two)
    elif sign in ["/", "divide", "Divide", "DIVIDE", "over", "Over", "OVER"]:
        result = int(number_one) / int(number_two)
    else:
        print("Invalid sign")
        result = "Invalid sign"
    
    print(f"Your answer is {result}!")
    print("Do you want to do another calculation?")
    answer = input("Yes or No:")
    if answer in ["No", "no", "NO"]:
        break
    else:
        continue

