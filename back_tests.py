import back
import os
import unittest


class BackTest(unittest.TestCase):
    """Tests for Mail list database"""
    def setUp(self):
        self.database = back.Database("Dummy List")

    def test_creation(self):
        self.assertEqual("Dummy List", self.database.get_name())

    def test_add_subscriber(self):
        self.database.add_subscriber("person", "person@has_subscriber_with_email")
        self.assertEqual(1, self.database.get_length())

    def test_add_already_existing_subscriber(self):
        self.database.add_subscriber("person", "person@email")
        self.assertEqual(1, self.database.get_length())
        self.assertEqual("A person with the given name person or given email person@email already exists", self.database.add_subscriber("person", "person@email"))
        self.assertEqual(1, self.database.get_length())

    def test_remove_existing_subscriber(self):
        self.database.add_subscriber("person", "person@email")
        self.assertEqual(1, self.database.get_length())
        self.database.remove_subscriber("person")
        self.assertEqual(0, self.database.get_length())

    def test_remove_non_existing_subscriber(self):
        self.assertFalse(self.database.remove_subscriber("person"))

    def test_has_subscriber_with_existing_email(self):
        self.database.add_subscriber("person", "person@email")
        self.assertEqual(1, self.database.get_length())
        self.assertTrue(self.database.has_subscriber_with_email("person@email"))

    def test_has_subscriber_with_non_existing_email(self):
        self.assertFalse(self.database.has_subscriber_with_email("fail@fail.com"))

    def test_get_subscribers(self):
        self.database.add_subscriber("person", "person@email")
        expected = [("person", "person@email")]
        self.assertEqual(expected, self.database.get_subscribers())

    def test_get_name(self):
        self.assertEqual("Dummy List", self.database.get_name())

    def test_get_filename(self):
        self.assertEqual("Dummy_List", self.database.get_file_name())

    def test_prepare_for_save(self):
        self.database.add_subscriber("Person", "person@email")
        self.assertEqual(sorted(["Person - person@email"]), self.database.prepare_for_save())

    def test_save(self):
        self.database.add_subscriber("Person", "person@email")
        self.database.save()
        self.assertTrue(os.path.exists("Lists"))
        self.assertTrue(os.path.exists("Lists/Dummy_List"))
        os.remove("Lists/Dummy_List")

if __name__ == '__main__':
    unittest.main()
