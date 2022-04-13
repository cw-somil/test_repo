import unittest
from src.utilities import utilities


class TestUtilities(unittest.TestCase):
    def test_get_value_from_label_clean(self):
        label = " |  bikE1=2 | bike2=4 |"
        res = utilities.get_value_from_label(label, "bike1", "NA")
        self.assertEqual(res, "2")

    def test_get_value_from_label_default(self):
        label = " |  bikE1=2 | bike2=4 |"
        res = utilities.get_value_from_label(label, "bike3", "NA")
        self.assertEqual(res, "NA")



if __name__ == '__main__':
    unittest.main()
