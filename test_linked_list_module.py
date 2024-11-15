import unittest
from linked_list_module import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_insert_and_str(self):
        self.list.insert(1)
        self.list.insert(2)
        self.list.insert(3)
        self.assertEqual(str(self.list), "1 2 3 ")

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.insert(1)
        self.assertEqual(self.list.size(), 1)
        self.list.insert(2)
        self.list.insert(3)
        self.assertEqual(self.list.size(), 3)

    def test_remove_duplicates(self):
        self.list.insert(1)
        self.list.insert(2)
        self.list.insert(2)
        self.list.insert(3)
        self.list.insert(1)
        self.list.remove_duplicates()
        self.assertEqual(str(self.list), "1 2 3 ")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            str(self.list)
        self.assertEqual(self.list.size(), 0)
        self.list.remove_duplicates()  # Should not raise an error


if __name__ == '__main__':
    unittest.main()
