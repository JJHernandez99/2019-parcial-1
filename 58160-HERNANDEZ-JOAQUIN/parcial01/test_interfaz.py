import unittest 
from interfaz import interfaz

class TestHexadecimalNumber(unittest.TestCase):

    def test_decimal_5_to_Hexa(self):
       result = interfaz(5)
       self.assertEqual(result,'005')
    
    def test_decimal_10_to_Hexa(self):
       result = interfaz(10)
       self.assertEqual(result,'00A')

class test_decimal_to_hexa_interfaz_1(unittest.TestCase):
    def test_decimal_1(self):
        result = interfaz(-17)
        self.assertEqual(result, 'Por favor,Ingrese un numero positivo')

class test_decimal_to_hexa_interfaz_2(unittest.TestCase):

    def test_decimal_1(self):
        result = interfaz('afasf')
        self.assertEqual(result, 'Por favor, Ingrese un numero')

class test_decimal_to_hexa_interfaz_3(unittest.TestCase):

    def test_decimal_1(self):
        result = interfaz('')
        self.assertEqual(result, 'Por favor, Ingrese un numero')
    
    
    
if __name__ == "__main__":
    unittest.main()
