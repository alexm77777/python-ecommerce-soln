from unittest import TestCase
from ..cart import Cart
from ..selection import Selection


class TestCart(TestCase):
    def test_create_cart(self):
        c = Cart('alice')
        self.assertEqual(c.user, 'alice')
        self.assertListEqual(c.selections, [])

    def test_add_selection_to_cart(self):
        c = Cart('alice')
        s = Selection('apple', 3, 10)
        c.add(s)
        self.assertEqual(len(c.selections), 1)
        self.assertIsInstance(c.selections[0], Selection)

    def test_empty_cart(self):
        c = Cart('alice')
        s = Selection('apple', 3, 10)
        c.add(s)
        c.empty()
        self.assertEqual(len(c.selections), 0)

    def test_total_cart(self):
        c = Cart('alice')
        s1 = Selection('apple', 3, 10)
        s2 = Selection('pear', 2, 5)
        c.add(s1)
        c.add(s2)
        self.assertEqual(c.total(), 40)

    def test_iterate_cart(self):
        c = Cart('alice')
        self.assertTrue(iter(c))
