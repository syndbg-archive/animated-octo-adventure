# DOCUMENTATION


# IMPORTS
from os import remove
import maillist
import maillist_database
import unittest


# main
class MaillistDB_Test(unittest.TestCase):
    def setUp(self):
        self.dummy_maillist = maillist.MailList("Dummy List")
        self.filename = self.dummy_maillist.get_name()
        db = maillist_database.MailListDatabase()
        db.write_maillist(self.dummy_maillist)

    def test_write_maillist(self):
        self.list.add("RadoRado", "radorado@hackbulgaria.com")
        opened_file = open(self.filename, "r")
        contents = opened_file.read()
        opened_file.close()
        self.assertEqual("RadoRado - radorado@hackbulgaria.com", contents)

    def tearDown(self):
        remove(self.filename)

# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
