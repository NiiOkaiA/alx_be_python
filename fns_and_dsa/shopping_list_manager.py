

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


shopping_list=[]

def main():
  while True:
    display_menu()
    global shopping_list
    choice = input("Enter your choice: ")

    if choice == '1':
        add=input("What do you want to add to the list: ")
        shopping_list.append(add)

    if choice =='2':
        remove=input("What should I remove?: ")
        shopping_list.remove(remove)
        
    if choice == '3':
        print(shopping_list)

    if choice == '4':
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()
     
        
