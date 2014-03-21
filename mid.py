from sys import exit
from glob import glob
import back


class Interface():
    """Mail list interface"""
    def __init__(self):
        self.mail_lists = []
        self.update_mail_lists(self.mail_lists)

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def trigger_show_lists(self):
        output = []
        i = 1
        for mail_object in self.mail_lists:
            output.append("[{}] {}".format(i, mail_object._name))
            i += 1
        return "\n".join(output)

    def trigger_show_list(self, unique_list_identifier):
        try:
            return self.mail_lists[int(unique_list_identifier) - 1].show_subscribers()
        except IndexError:
            return "List with unique identifier {} was not found!".format(unique_list_identifier)

    def trigger_add_to_list(self, unique_list_identifier):
        desired_list = self.mail_lists[int(unique_list_identifier) - 1]
        name = str(input("name>"))
        email = str(input("email>"))
        desired_list.add_subscriber(name, email)
        desired_list.save()
        return "{} was added to {}".format(name, desired_list._name)

    # def trigger_remove_subscriber_from_list(self, unique_list_identifier, subscriber_name):
    #     desired_list = self.mail_lists[int(unique_list_identifier)-1]
    #     desired_list.remove_subscriber(subscriber_name)

    def trigger_create_list(self, list_name):
        mail_list = back.Database(list_name)
        self.mail_lists.append(mail_list)
        mail_list.save()
        return "New list <{}> was created".format(list_name)

    def update_mail_lists(self, mail_lists):
        files = glob("./Lists/*")
        for filename in files:
            opened_file = open(filename, "r")
            contents = opened_file.read().split()
            filename = filename.split("/")
            filename = filename[2]
            maillist = back.Database(filename)
            for line in contents:
                print(line)
                # contents = contents.split("-")
                # print(contents)
                # for line in contents:
                #     print(line)
                #     maillist.add_subscriber(line[0], line[1])
                # self.mail_lists.append(maillist)
            opened_file.close()

    def trigger_welcome(self):
        welcome_message = [
            "Hello Stranger! This is a cutting-edge, console-based mail-list!",
            "Type help, to see a list of commands."]
        return "\n".join(welcome_message)

    def trigger_help(self):
        help_message = ["Here is a full list of commands:",
                        "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                        "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                        "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                        "* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list",
                        "* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list",
                        "* create <list_name> - Creates a new empty list, with the given name.",
                        "* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.",
                        "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                        "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                        "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                        "* exit - this will quit the program"]
        return "\n".join(help_message)

    def trigger_exit(self):
        exit("Exiting")

    def trigger_unknown_command(self):
        return "Error: Unknown command. Type help to see available commands"
