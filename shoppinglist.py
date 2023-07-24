def create_shopping_list():
    return []

def add_item(shopping_list, item):
    shopping_list.append(item)

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)

def view_shopping_list(shopping_list):
    for item in shopping_list:
        print(item)

def shopping_list_app():
    shopping_list = create_shopping_list()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add item to shopping list.")
        print("2. Remove item from shopping_list.")
        print("3. View shopping list.")
        print("4. Quit.")
        option = input("Choose an option: ")
        if option == "1":
            item = input("Enter an item to add: ")
            add_item(shopping_list, item)
        elif option == "2":
            item = input("Enter an item to remove: ")
            remove_item(shopping_list, item)
        elif option == "3":
            view_shopping_list(shopping_list)
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")

def test_shopping_list_app():
    shopping_list = create_shopping_list()
    add_item(shopping_list, "Apples")
    add_item(shopping_list, "Bananas")
    view_shopping_list(shopping_list)
    remove_item(shopping_list, "Apples")
    view_shopping_list(shopping_list)
