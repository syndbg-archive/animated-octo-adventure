# IMPORTS
import mid


# main
def main():
    main = mid.Interface()

    print(main.trigger_welcome())
    while True:
        command = main.parse_command(input(">"))

        if main.is_command(command, "help"):
            print(main.trigger_help())

        elif main.is_command(command, "show_lists"):
            print(main.trigger_show_lists())

        elif main.is_command(command, "show_list"):
            print(main.trigger_show_list(command[1]))

        elif main.is_command(command, "add"):
            print(main.trigger_add_to_list(command[1]))

        elif main.is_command(command, "create"):
            print(main.trigger_create_list(command[1]))

        elif main.is_command(command, "remove_subscriber"):
            main.trigger_remove_subscriber_from_list(command[1], command[2])

        # elif main.is_command(command, "search_email"):
        #     main.trigger_search_email(command)

        # elif main.is_command(command, "merge_lists"):
        #     main.trigger_merge_lists(command)

        # elif main.is_command(command, "export"):
        #     main.trigger_export()

        elif main.is_command(command, "exit"):
            main.trigger_exit()

        else:
            print(main.trigger_unknown_command())


if __name__ == '__main__':
    main()
