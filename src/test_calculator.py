import unittest
from calculator import multiply

class TestSomething(unittest.TestCase):
    def test.multiply(self):
        self.assertEqual(6, multiply(2,3))

if __name__ == '__main__':
    unittest.main