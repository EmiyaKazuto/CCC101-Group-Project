import unittest
import math
from calcu_logic import Calculator

class TestCalculator(unittest.TestCase):

    def test_append_operator(self):

        c = Calculator()
        
        result = c.add(10,5)
        result2 = c.subtract(11,8)
        result3 = c.multiply(4,3)
        result4 = c.divide(6,2)

        self.assertEqual(result, 15)
        self.assertEqual(result2, 3)
        self.assertEqual(result3, 12)
        self.assertEqual(result4, 3)
        self.assertRaises(ZeroDivisionError, c.divide(1,0))
        self.assertRaises(ValueError, c.divide, 4,0)
    
    def test_add_to_expression(self):

        c = Calculator()

        ans = c.add(10,5,1)
        
        self.assertEqual(c.current_expression, 16)
    
    def test_pi_function(self):
        
        c = Calculator()

        π = 3.141592653589793
        π = math.pi
        
        self.assertTrue(π == 3.1416 or π == 3.14)
        self.assertEqual(c.add(3, π), 6.141592652)
        self.assertEqual(c.multiply(4,π), 12.56637061)
    
    def test_log_function(self):
        
        c = Calculator()
        
        log = math.log10
        
        self.assertEqual(c.log(10), 1)
        self.assertRaises(ValueError, c.log(0))
    
    def test_ln_function(self):
        
        c = Calculator()

        ln = math.log1p

        self.assertEqual(c.ln(10), 2.302585093)

    def test_abs_function(self):

        c = Calculator()

        self.assertEqual(c.abs(1), 1)
        self.assertEqual(c.abs(-1), 1)
    
    def test_e_function(self):

        c = Calculator()

        e = math.e

        self.assertEqual(c.e(5), 148.4131591)
        self.assertEqual(c.e(0), 1)

    def test_trig_sine(self):

        c = Calculator

        sin = math.sin

        self.assertEqual(c.sin(30), 0.5)
        self.assertEqual(c.sin(60), 0.8660254038)
        self.assertEqual(c.sin(90), 1)
    
    def test_trig_cosine(self):
         
         c = Calculator()

         cos = math.cos

         self.assertEqual(c.cos(30), 0.8660254038)
         self.assertEqual(c.cos(60), 0.5)
         self.assertEqual(c.cos(90), 0)
    
    def test_trig_tan(self):

        c = Calculator()

        tan = math.tan

        self.assertEqual(c.tan(30), 0.5773502692)
        self.assertEqual(c.tan(60), 1.732050808)
        self.assertRaises(ValueError, c.tan(90))
    
    def test_squared(self):

        c = Calculator()

        self.assertEqual(c.squared(2,2), 4)
        self.assertEqual(c.squared(3,2), 9)

    def test_sqrt(self):

        c = Calculator()

        sqrt = math.sqrt

        self.assertEqual(c.sqrt(25), 5)
        self.assertEqual(c.sqrt(36), 6)
        self.assertEqual(c.sqrt(81), 9)
    
    def test_cubed(self):

        c = Calculator()

        self.assertEqual(c.cubed(2), 8)
        self.assertEqual(c.cubed(4), 64)
    
    def test_perm(self):

        c = Calculator()

        self.assertEqual(c.perm(3,2), 6)
        self.assertRaises(ValueError, c.perm, 2,3)
    
    def test_comb(self):

        c = Calculator()

        self.assertEqual(c.comb(3,2), 3)
        self.assertRaises(ValueError, c.comb, 2,3)
    
    def test_clear(self):
        pass


    def test_delete(self):
        pass


    def test_answer(self):
        pass


    def test_exp_function(self):
        pass


    def test_evaluate(self):
        pass




        
if __name__ == "__main__":
	unittest.main() 
	
"""
## RAN 8 TESTS - OK
import unittest
import math
from logic import Calculator


class TestCalculator(unittest.TestCase):

    def test_add_to_expression(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        # Test if the current expression matches the combination of the inputted numbers
        self.assertEqual(c.current_expression, '123')

    def test_append_operator(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(3)
        # Append an operator to the expression
        c.append_operator('+')
        # Test if the operator was appended to the total expression
        self.assertEqual(c.total_expression, '123+')
        # Test if the current expression is cleared
        self.assertEqual(c.current_expression, '')

    def test_evaluate_expression_add(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('+')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '20')

    def test_evaluate_expression_subtract(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('-')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '0')
    
    def test_evaluate_expression_Multiply(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('*')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '100')

    def test_evaluate_expression_Divide(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('/')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.evaluate()
        # Test if the calculator evaluates the expression correctly
        self.assertEqual(c.current_expression, '1.0')
    
    def test_evaluate_expression_add_and_subtract(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('+')
        # Add additional numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Append an operator to the expression
        c.append_operator('-')
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(2)
        c.add_to_expression(0)
        # Test if the calculator evaluates the expression correctly
        c.evaluate()
        self.assertEqual(c.current_expression, '-10')

    def test_square_a_number(self):

        c = Calculator()
        # Add some numbers to the current expression
        c.add_to_expression(1)
        c.add_to_expression(0)
        # Square the inputted number
        c.squared()
        c.evaluate()
        # Test if the calculator gives the correct result
        self.assertEqual(c.current_expression, '100')


if __name__ == "__main__":
    unittest.main()
"""