import mid
import unittest


class MidTest(unittest.TestCase):
    """Tests for Mail list interface"""
    def setUp(self):
        self.interface = mid.Interface()

    # def test_trigger_create_list(self):

    def test_trigger_welcome(self):
        self.assertEqual("Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands.", self.interface.trigger_welcome())

    def test_trigger_help(self):
        self.assertEqual("Here is a full list of commands:\n* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier\n* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>\n* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.\n* create <list_name> - Creates a new empty list, with the given name.\n* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.\n* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.\n* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.\n* exit - this will quit the program", self.interface.trigger_help())

    def test_trigger_unknown_command(self):
        self.assertEqual("Error: Unknown command. Type help to see available commands", self.interface.trigger_unknown_command())


if __name__ == '__main__':
    unittest.main()
