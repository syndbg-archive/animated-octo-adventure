from sys import exit
from glob import glob
from commandparser import CommandParser
from back import Database
from os import remove


class Interface():
    """Mail list interface"""
    def __init__(self):
        self.cp = CommandParser()
        self.mail_lists = []
        self.update_mail_lists(self.mail_lists)
        self._init_callbacks()
        self._loop()

    def callback_show_lists(self, arguments):
        output = []
        for i, mail_object in enumerate(self.mail_lists):
            output.append("[{}] {}".format(i+1, mail_object._name))
        return "\n".join(output)

    def callback_show_list(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        try:
            return self.mail_lists[unique_list_identifier].show_subscribers()
        except IndexError:
            return "List with unique identifier {} was not found!".format(unique_list_identifier+1)

    def callback_add_subscriber(self, arguments):
        unique_list_identifier = arguments[0]
        desired_list = self.mail_lists[int(unique_list_identifier) - 1]
        name = str(input("name>"))
        email = str(input("email>"))
        if desired_list.add_subscriber(name, email) is True:
            desired_list.save("file")
            return "{} was added to {}.".format(name, desired_list._name)
        return "Subscriber with email <{}> already exists.".format(email)

    def callback_remove_subscriber(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        subscriber_id = int(arguments[1]) - 1
        desired_list = self.mail_lists[unique_list_identifier]
        subscriber_name = desired_list.get_subscriber_name(subscriber_id)
        if desired_list.remove_subscriber(subscriber_name) is True:
            desired_list.save("file")
            return "<{}> was removed from <{}>.".format(subscriber_name, desired_list._name)
        return "Subscriber <{}> was not found in <{}>.".format(subscriber_name, desired_list._name)

    def callback_update_subscriber(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        subscriber_id = int(arguments[1]) - 1
        desired_list = self.mail_lists[unique_list_identifier]
        subscriber_name = desired_list.get_subscriber_name(subscriber_id)
        subscriber_email = desired_list.get_subscriber_email(subscriber_id)
        print("Updating <{}> - <{}>\nPress Enter if you want the field to remain the same".format(subscriber_name, subscriber_email))
        new_name = input("new name>")
        new_email = input("new email>")

        if new_name == "":
            if new_email == "":
                return "Nothing to update."
            else:
                desired_list.update_subscriber(subscriber_name, subscriber_name, new_email)
                desired_list.save("file")
                return "Updated <{}> - <{}>.".format(subscriber_name, new_email)
        elif new_email == "":
            if new_name == "":
                return "Nothing to update."
            else:
                desired_list.update_subscriber(subscriber_name, new_name, subscriber_email)
                desired_list.save("file")
                return "Updated <{}> - <{}>.".format(new_name, subscriber_email)
        else:
            desired_list.update_subscriber(subscriber_name, new_name, new_email)
            desired_list.save("file")
            return "Updated <{}> - <{}>.".format(new_name, new_email)

    def callback_create_maillist(self, arguments):
        list_name = arguments[0]
        mail_list = Database(list_name)
        self.mail_lists.append(mail_list)
        mail_list.save("file")
        return "New list <{}> was created.".format(list_name)

    def callback_delete_maillist(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        desired_list = self.mail_lists[unique_list_identifier]
        if desired_list.remove_list() is True:
            return "{} was deleted.".format(desired_list.get_name())
        return "You crazy bastard. Stop playing with fire!"

    def callback_update_maillist(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        new_list_name = arguments[1]
        to_be_deleted_list = self.mail_lists[unique_list_identifier]
        old_name = to_be_deleted_list._name
        old_subscribers = to_be_deleted_list._subscribers
        self.mail_lists.pop(unique_list_identifier)
        mail_list = Database(new_list_name)
        mail_list._subscribers = old_subscribers
        self.mail_lists.append(mail_list)
        mail_list.save("file")
        remove("./Lists/{}".format(to_be_deleted_list.get_file_name()))
        return "Updated <{}> to <{}>".format(old_name, mail_list._name)

    def callback_search_by_email(self, arguments):
        found_in_lists = []
        needle_email = arguments[0]
        for maillist_object in self.mail_lists:
            if maillist_object.has_subscriber_with_email(needle_email) is True:
                found_in_lists.append(maillist_object._name)
        return "\n".join(found_in_lists)

    def callback_merge_lists(self, arguments):
        list_id_a = int(arguments[0]) - 1
        list_id_b = int(arguments[1]) - 1
        new_list_name = arguments[2]
        list_a = self.mail_lists[list_id_a]
        list_b = self.mail_lists[list_id_b]
        a_subscribers = list_a._subscribers
        b_subscribers = list_b._subscribers
        a_name = list_a._name
        b_name = list_b._name
        mail_list = Database(new_list_name)
        mail_list._subscribers = dict(a_subscribers, **b_subscribers)
        self.mail_lists.append(mail_list)
        return "Merged <{}> and <{}> into <{}>".format(a_name, b_name, new_list_name)

    def callback_export_json(self, arguments):
        unique_list_identifier = int(arguments[0]) - 1
        desired_list = self.mail_lists[unique_list_identifier]
        desired_list.save("json")
        return "Exported <{}> to <{}.json>".format(desired_list.get_name(), desired_list.get_file_name())

    def callback_welcome(self):
        return "Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands."

    def callback_help(self, arguments):
        help_message = ("Here is a full list of commands:",
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
                        "* exit - this will quit the program")
        return "\n".join(help_message)

    def callback_exit(self):
        exit("Exiting.")

    def update_mail_lists(self, arguments):
        for filename in self.fetch_maillists():
            opened_file = open(filename, "r")
            contents = opened_file.readlines()
            filename = filename.split("/")[2]
            maillist = Database(filename)
            for record in contents:
                record = record.split(" - ")
                maillist.add_subscriber(record[0], record[1].rstrip())
            self.mail_lists.append(maillist)
            opened_file.close()

    def fetch_maillists(self):
        return glob("./Lists/*[!.json]")

    def _init_callbacks(self):
        print(self.callback_welcome())
        self.cp.on("show_lists", self.callback_show_lists)
        self.cp.on("show_list", self.callback_show_list)
        self.cp.on("add", self.callback_add_subscriber)
        self.cp.on("update_subscriber", self.callback_update_subscriber)
        self.cp.on("remove_subscriber", self.callback_remove_subscriber)
        self.cp.on("create", self.callback_create_maillist)
        self.cp.on("update", self.callback_update_maillist)
        self.cp.on("search_email", self.callback_search_by_email)
        self.cp.on("merge", self.callback_merge_lists)
        self.cp.on("export", self.callback_export_json)
        self.cp.on("help", self.callback_help)
        self.cp.on("exit", self.callback_exit)

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)
