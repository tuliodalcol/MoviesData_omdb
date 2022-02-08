import unittest
from modules.etl import string2float

class Testcase1(unittest.TestCase):
        
    def test_string2float_is_float(self):
        self.assertIsInstance(string2float('%30'), float)
        self.assertIsInstance(string2float('1/10'), float)
        self.assertIsInstance(string2float('3'), float)
        self.assertIsInstance(string2float('3.3'), float)
        self.assertIsInstance(string2float(3), float)
        self.assertIsInstance(string2float(3.3), float)

if __name__ == "__main__":
    unittest.main()
