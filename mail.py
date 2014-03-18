def parse_command(command):
    return tuple(command.split(" "))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Try one of the following:",
                       " show_lists",
                       " show_list <unique_list_identifier>",
                       " add <unique_list_identifier>",
                       " create <list_name>",
                       " search_email <email>",
                       " merge_lists <list_identifier_1> <list_identifier_2> <new_list_name>",
                       " export <unique_list_identifier>",
                       " exit"]
    print("\n".join(unknown_command))


def main():
    while True:
        command = parse_command(input("Enter command>"))


        else:
            trigger_unknown_command()

if __name__ == '__main__':
    main()
