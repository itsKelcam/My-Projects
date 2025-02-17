def calculate_area():
    x = input("Enter your width.")
    y = input("Enter another height.")
    a = input("Enter your depth if you have one, if not press ENTER to skip.")
    
    if a:
        a = float(a)
        z = float(x) * float(y) * a
    else:
        z = float(x) * float(y)

    print(f"The calculated area is {z}!")

calculate_area()

