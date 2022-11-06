import unittest
import postcodes


class PostcodeCheckerTestCase(unittest.TestCase):
    """ Unit test testcase class for the Postcode Checker """

    def setUp(self):
        print("Setting up...")
        self.obj = postcodes.PostcodeChecker()

    def test_check_code(self):
        """ Tests the check_code method """

        # Test cases:
        pcode1 = "L1 8JQ"
        pcode2 = "SW1W 0NY"
        pcode3 = "PO16 7GZ"
        pcode4 = "POAA 7GZ"
        self.assertEqual(self.obj.check_code(pcode1), True)
        self.assertEqual(self.obj.check_code(pcode2), True)
        self.assertEqual(self.obj.check_code(pcode3), True)
        self.assertEqual(self.obj.check_code(pcode4), False)


if __name__ == "__main__":
    unittest.main()

    
