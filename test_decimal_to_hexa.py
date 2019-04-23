import unittest 
from decimal_to_hexa import decimal_to_hexa

class TestHexadecimalNumber(unittest.TestCase):

    def test_decimal_5_to_Hexa(self):
       result = decimal_to_hexa(5)
       self.assertEqual(result,'005')
    
    def test_decimal_10_to_Hexa(self):
       result = decimal_to_hexa(10)
       self.assertEqual(result,'00A')

    def test_decimal_234_to_Hexa(self):
       result = decimal_to_hexa(234)
       self.assertEqual(result,'0EA')
       
    def test_decimal_HOLA_to_Hexa(self):
       result = decimal_to_hexa('HOLA')
       self.assertEqual(result,'Error, NO INGRESO UN NUMERO')

    def test_decimal_1234_to_Hexa(self):
       result = decimal_to_hexa(1234)
       self.assertEqual(result,'4D2')

    
if __name__ == "__main__":
    unittest.main()


    