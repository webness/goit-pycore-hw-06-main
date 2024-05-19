import handler

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            print(handler.list_all_contacts())

        elif command == "add":
            print(handler.add_phone_number(*args))

        elif command == "change":
            print(handler.update_phone_number(*args))

        elif command == "contact":
            print(handler.retrieve_contact(*args))

        elif command == "delete":
            print(handler.remove_contact(*args))

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command. Usage: hello | all | add [name] [phone] | "\
                  "change [name] [phone] | contact [name] | delete [name] | exit | close")

if __name__ == "__main__":
    main()
