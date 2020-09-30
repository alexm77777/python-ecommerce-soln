from unittest import TestCase
from ..selection import Selection


class TestSelection(TestCase):
    def test_create_selection(self):
        s = Selection('apple', 3, 10)
        self.assertDictEqual(s.__dict__, {
            'name': 'apple',
            'price': 3,
            'amount': 10
        })

    def test_selection_to_string(self):
        s = Selection('apple', 3, 10)
        string = str(s)
        self.assertEqual(string, "apple @ $3.00 x 10")
