import os
from address_repo import AddressRepo

global address_book
address_book = None

addressRepo = AddressRepo()

def display_address():
    print("Address Book\n".rjust(40))
    for bookEntry in addressRepo.get_address()["address-book"]:
        print("{}\t| {}\t| {}\t| {}".format(
            str(bookEntry.get("name")).rjust(10).center(2),
            str(bookEntry.get("address")).rjust(10).center(2),
            str(bookEntry.get("contact")).rjust(10).center(2),
            str(bookEntry.get("email")).rjust(10).center(2)))

def add_new_address():
    print("Add new address book: ")
    while True:
        name = input("Name: ")
        if name != "":
            break
        print("Please input a name.")
    while True:
        address = input("Address: ")
        if address != "":
            break
        print("Please input a address.")
    contact = input("Contact: ")
    email = input("Email: ")
    new_entry = {
        "name": name,
        "address" : address,
        "contact" : contact,
        "email" : email,
    }
    print("\nSuccessfully Added!")
    addressRepo.add_new_address(new_entry)


def update_address():
    print("UPDATE ADDRESS")
    print("-"*15)
    # display_edit_screen(search_address_book())
    search_address_book()

def delete_address():
    print("DELETE ADDRESS")
    print("-"*15)

    result = search_address_book()

    if result != None:
        while True:
            response = input("Enter Y or N: ")
            if response.lower() == "y":
                print("record to delete -> {}".format(result))
                addressRepo.delete_address(result)
                break
            elif response.lower() == "n":
                input("quit")
                break
            else:
                print("Invalid input")

def display_edit_screen(record_for_edit):
    
    # if record_for_edit == None:
    #     return

    get_user_input = lambda input, default : input if input != "" else default

    name = record_for_edit.get("name")
    address = record_for_edit.get("address")
    contact = record_for_edit.get("contact")
    email = record_for_edit.get("email")
    
    print("Edit Address")
    name = get_user_input(input("New Name [{}]: ".format(name)),name)
    address = get_user_input(input("New Address [{}]: ".format(address)),address)
    contact = get_user_input(input("New Contact [{}]: ".format(contact)),contact)
    email = get_user_input(input("New Email [{}]: ".format(email)),email)

    record_for_edit["name"] = name
    record_for_edit["address"] = address
    record_for_edit["contact"] = contact
    record_for_edit["email"] = email

    addressRepo.update_address(record_for_edit)


def search_address_book():
    print("Search Address Book: ")

    name = input("\tName: ")
    address = input("\tAddress: ")

    result = addressRepo.find_address_book(name, address)
    record_for_edit ={}

    if len(result) > 1:
        display_search_result(result)
        while True:
            id = int(input("Enter a ID to Edit [1-{}]: ".format(len(result))))
            if id > len(result):
                print("Invalid Selection, Try Again")
            else:
                record_for_edit = result[id - 1]
                break
            #new add
        display_edit_screen(record_for_edit)
    elif len(result) == 1:
        record_for_edit = result[0]
        display_search_result(result)
        #return relocate
        return record_for_edit
    else:
        print("User Not Found")

    # return record_for_edit


def search_address():
    print("Search Address Book333: ")

    name = input("\tName: ")
    address = input("\tAddress: ")
    
    result = addressRepo.find_address_book(name, address)
    record_for_edit ={}
    
    display_search_result(result)

    return record_for_edit

def display_search_result(result):
    index = 1
    for entry in result:
        print("{} | {} | {} | {} | {}".format(
            str(index).center(3),
            str(entry.get("name")).rjust(20),
            str(entry.get("address")).rjust(20),
            str(entry.get("contact")).rjust(20),
            str(entry.get("email")).rjust(20)))
        index = index + 1
        
            
def back():
    while True:
        back_menu = str(input("\nWould you like to go back to menu? (Y/N) : "))
        if (back_menu.lower() == 'y'):
            clear_screen()
            display_menu()
        elif (back_menu.lower() == 'n'):
            break
        else:
            print("Invalid input, input must be (Y/N)")


def display_menu():

        print("\n*** ADDRESS-BOOK APP MENU ****\n")
        print("\t1. Display Address ")
        print("\t2. Create New Address ")
        print("\t3. Search Address ")
        print("\t4. Update Address ")
        print("\t5. Delete Address ")
        print("\t6. Exit ")

        selection = input("\n\033[1;33;40m Input A Selection: ")
        if selection == '1':
            clear_screen()
            display_address()
            back() 
        elif selection == '2':
            clear_screen()
            add_new_address()
            back()
        elif selection == '3':
            clear_screen()
            search_address()
            back()
        elif selection == '4':
            clear_screen()
            update_address()
            back()
        elif selection == '5':
            clear_screen()
            delete_address()
            back()
        elif selection == '6':
            clear_screen()
          
def clear_screen():
    os.system("cls")

clear_screen()
display_menu()
