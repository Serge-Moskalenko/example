from components.tools import bot_command
from components.tools import parse_input
from components.data_action import save_data,load_data
from components.functions import add_birthday,add_contact,change_number,print_phone,show_birthday,birthdays


def main():
    contacts = load_data()
    print("Welcome to the assistant bot!")
    print("Available commands:\nhello\nadd\nall\nchange\nphone\nadd_birthday\nshow_birthday\nbirthday\nclose or exit")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in(bot_command.exit, bot_command.close):
            save_data(contacts)
            print("Good bye!")
            break
        elif command == bot_command.hello:
            print("How can I help you?")
        elif command == bot_command.add:
            print(add_contact(args, contacts))
        elif command == bot_command.all:
            print(contacts)
        elif command == bot_command.change:
            print(change_number(args, contacts))
        elif command == bot_command.phone:
            print(print_phone(args, contacts))
        elif command == bot_command.add_birthday:
            print(add_birthday(args, contacts))
        elif command == bot_command.show_birthday:
            print(show_birthday(args, contacts))
        elif command == bot_command.birthday:
            print(birthdays(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}")