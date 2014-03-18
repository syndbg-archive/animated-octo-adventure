def parse_command(command):
    return tuple(command.split(" "))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Try one of the following:",
                       "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                       "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                       "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                       "* create <list_name> - Creates a new empty list, with the given name.",
                       "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                       "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                       "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                       "* exit - this will quit the program]",
    print("\n".join(unknown_command))


def main():
    while True:
        command = parse_command(input(
            "Hello Stranger! This is a cutting-edge, console-based mail-list!",
            "Type help, to see a list of commands."))

        if is_command(command, "show_lists"):
            trigger_show_lists(command)

        elif is_command(command, "show_list"):
            trigger_show_list(command)

        elif is_command(command, "add"):
            trigger_add(command)

        elif is_command(command, "create"):
            trigger_create(command)

        elif is_command(command, "search_email"):
            trigger_search_email(command)

        elif is_command(command, "merge_lists"):
            trigger_merge_lists(command)

        elif is_command(command, "export"):
            trigger_export(command)

        elif is_command(command, "exit"):
            trigger_exit(command)

if __name__ == '__main__':
    main()
