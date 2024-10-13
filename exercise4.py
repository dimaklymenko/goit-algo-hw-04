def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    except:
        return print("Помилка. Ім'я не знайдено")    

def show_phone(args, contacts):
    try:
        args = args[0]
        # return contacts.get(args)
        return contacts[args]
    except:
        return print("Помилка. Ім'я не знайдено")    

def show_all(contacts):
    return contacts    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))         
            else:
                print("Invalid command.")
        except ValueError :
            continue            

if __name__ == "__main__":
    main()
