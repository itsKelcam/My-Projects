# Initialize the class dictionary
math_class = dict()

# Function to add a student
def add_a_student():
    try:
        name = input("Please enter the name of the student you would like to add: ")
        grade = float(input("Please enter their grade in your class: "))  # Convert grade to float
        math_class[name] = grade  # Correct way to add to dictionary
        print(f"{name} with the grade of {grade} has been added successfully!")
    except Exception as e:
        print(f"Something went wrong! Error: {e}")

# Function to update a student's grade
def update_a_grade():
    try:
        name = input("Whose grade would you like to update? ")
        if name in math_class:
            new_grade = float(input("Enter the new grade: "))
            math_class[name] = new_grade
            print(f"{name}'s grade has been updated to {new_grade}.")
        else:
            print("There is no student in your records with that name!")
    except Exception as e:
        print(f"Something went wrong! Error: {e}")

# Function to calculate the class average
def calculate_average():
    try:
        if math_class:  # Check if there are any students in the class
            average = sum(math_class.values()) / len(math_class)
            print(f"Your class average is {average:.2f}!")
        else:
            print("No students in the class to calculate an average.")
    except Exception as e:
        print(f"Something went wrong! Error: {e}")

# Main function to run the program
def main():
    print("HOME SCREEN")
    print("Options: add, update, calculate, exit")
    while True:
        action = input("Please enter what you would like to do today: ").lower()

        if action == "add":
            add_a_student()
        elif action == "update":
            update_a_grade()
        elif action == "calculate":
            calculate_average()
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("That was not a valid response!")

# Run the program
main()
