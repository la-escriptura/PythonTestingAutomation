from CalcFunc import add, product, lcm
import unittest

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_product(self):
        self.assertEqual(product(2, 3), 6)
        self.assertEqual(product(-2, 3), -6)
        self.assertEqual(product(-2, -3), 6)
        self.assertEqual(product(0, 5), 0)

    def test_lcm(self):
        self.assertEqual(lcm(2, 5), 10)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(7, 3), 21)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
