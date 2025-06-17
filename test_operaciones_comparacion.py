import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales

class TestOperacionesComparacion(unittest.TestCase):

    def test_es_mayor_que(self):
        self.assertTrue(es_mayor_que(15, 14))  
        self.assertFalse(es_mayor_que(2, 6))    
        self.assertFalse(es_mayor_que(5, 5))  
        self.assertGreater(int(es_mayor_que(17, 7)), 0)  
        self.assertGreater(int(es_mayor_que(7, 3)), 0)  

    def test_es_menor_que(self):
        self.assertTrue(es_menor_que(1, 5))  
        self.assertTrue(es_menor_que(5, 10))  
        self.assertFalse(es_menor_que(17, 3))  
        self.assertFalse(es_menor_que(3, 3))  

    def test_es_mayor_o_igual_que(self):
        self.assertTrue(es_mayor_o_igual_que(15, 3))  
        self.assertTrue(es_mayor_o_igual_que(7, 7))  
        self.assertAlmostEqual(int(es_mayor_o_igual_que(18, 9)), 1)  
        self.assertGreaterEqual(es_mayor_o_igual_que(7, 7), True)  
        self.assertGreaterEqual(es_mayor_o_igual_que(50, 50), True)  

    def test_es_menor_o_igual_que(self):
        self.assertTrue(es_menor_o_igual_que(2, 8))  
        self.assertFalse(es_menor_o_igual_que(100, 1))  
        self.assertAlmostEqual(int(es_menor_o_igual_que(6, 7)), 1)  
        self.assertLessEqual(es_menor_o_igual_que(205, 1571), True)  
        self.assertLessEqual(es_menor_o_igual_que(5500, 450), False)  

    def test_son_iguales(self):
        self.assertTrue(son_iguales(7, 7))  
        self.assertFalse(son_iguales(6, 7))  
        self.assertTrue(son_iguales(8, 8))  
        self.assertNotEqual(son_iguales(50, 10), True)  

if __name__ == '__main__':
    unittest.main()
