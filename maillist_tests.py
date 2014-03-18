import maillist
import unittest


class MailListTest(unittest.TestCase):
    """Tests for MailList"""

    def setUp(self):
        self.list = maillist.MailList("Hack Bulgaria")

    def test_mail_list_creation(self):
        self.assertEqual("Hack Bulgaria",
                         self.list.get_name())

    def test_mail_list_add_subscriber(self):
        self.list.add("RadoRado", "radorado@hackbulgaria.com")

        self.assertEqual(1, self.list.get_length())

    def test_mail_list_get_subscribers(self):
        self.list.add("RadoRado", "radorado@hackbulgaria.com")
        expected = [("RadoRado", "radorado@hackbulgaria.com")]
        self.assertEqual(expected, self.list.get_subscribers())

    def test_mail_list_get_filename(self):
        self.assertEqual("Hack_Bulgaria", self.list.get_file_name())


if __name__ == '__main__':
    unittest.main()
