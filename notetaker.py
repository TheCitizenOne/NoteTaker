import os

def display_menu():
    print("Welcome to Note Taker.")
    print("---------------------")
    print("1- Create a new note")
    print("2- Edit a note")
    print("3- Read a note")
    print("4- Delete a note")
    print("5- Exit")

def main():
    while True:
        display_menu()
        opt = input("Select an option [1-5]: ")

        if opt == "1":
            create()
        elif opt == "2":
            edit()
        elif opt == "3":
            read_note()
        elif opt == "4":
            delete()
        elif opt == "5":
            print("Quitting...")
            exit()
        else:
            print("Please enter a number between 1-5.\n")
        

def create():
    note = input("Note: ")
    save(note)

def edit():
    x = input("Enter the name of file (with extension): ")
    if os.path.isfile(x):
        y = input("Enter your note: ")
        with open(f"{x}", "a") as file:
            file.write(y)
    else:
        print("File not found.")
    
def read_note():
    x = input("Enter the name of file (with extension): ")
    if os.path.isfile(x):
        with open(f"{x}", "r") as file:
            content = file.read()
            print(content)
            print()
    else:
        print("Please enter a valid name.\n")
        
        
def delete():
    x = input("Enter the name of file (with extension): ")
    try:
        auth = input("Are you sure? ('y' for yes, 'n' for no): ")
        if auth == "y":
            os.remove(x)
            print("Note deleted.\n")
        elif auth == "n":
            print("Process cancelled.\n")
        else:
            print("Please enter 'y' or 'n'.\n")
    except FileNotFoundError:
        print(f"'{x}' does not exist.\n")
    except PermissionError:
        print(f"Permission denied: unable to delete {x}.\n")
    except Exception as e:
        print(f"An error occured: {e}\n")
    
def save(x):
    file_name = input("Enter the name of new file: ")
    if os.path.isfile(f"{file_name}"):
        print("File exists.\n")
    else:
        with open(f"{file_name}", "w") as file:
            file.write(x)
            print("Note saved.\n")

if __name__=="__main__":
    main()
