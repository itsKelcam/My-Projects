to_do_list = []

while True:
    choice = input("Please enter one of the following options:\nView\nAdd\nRemove\nQuit\n: ")
    if choice == "Add":
        task = input("What would you like to add to your to-do list?")
        to_do_list.append(task)
    elif choice == "View":
        print(to_do_list)
    elif choice == "Remove":
        if to_do_list:
            for index, task in enumerate(to_do_list, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")
        removal_item = input("What would you like to remove from your list?")
        try:
            to_do_list.remove(removal_item)
            print("Item Removed!")
        except ValueError:
            print("Item not found in the to-do list.")
        print("Item not found in the to-do list.")
    elif choice == "Quit":
        break
    else:
            print("Please enter one of these following options: View, Add, Remove, or Quit")