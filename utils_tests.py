import unittest

class utils:
    def reverse(number):
        try:
            int(number)

        except:
            print("Please enter an integer, invalid input!")

        else:
            converted = str(number)
            reversed = converted[::-1]
            return reversed


    def formatter(number):
        try:
            check = int(number)

        except:
            print("Please enter an integer, invalid input!")
        
        else:
            
            return bin(check), oct(check)

class TestFunctions(unittest.TestCase):
    def test_int_rev(self):
        self.assertEqual(utils.reverse(123), "321")
    
    def test_string_rev(self):
        self.assertEqual(utils.reverse("hi"), None)
    
    def test_float_rev(self):
        self.assertEqual(utils.reverse(0.1), "1.0")

    def test_int_formatter(self):
        self.assertEqual(utils.formatter(10), ('0b1010' , '0o12'))

    def test_string_formatter(self):
        self.assertEqual(utils.formatter("hi"), None)
    
    def test_float_formatter(self):
        self.assertEqual(utils.formatter(0.2), None)

    
if __name__ == "__main__":
    unittest.main()