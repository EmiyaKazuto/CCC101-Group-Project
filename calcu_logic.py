from math import *

sin, cos, tan = math.sin, math.cos, math.tan
sqrt = math.sqrt
power = math.pow
π = math.pi
abs = math.fabs
log = math.log10
ln = math.log1p
e = math.e

class Calculator():
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)
    
    def log_function(self):
        self.current_expression = 'log(' + self.current_expression

    def ln_function(self):
        self.current_expression = 'ln(' + self.current_expression

    def abs_function(self):
        self.current_expression = 'abs(' + self.current_expression

    def trig_sine(self):
        self.current_expression =  'sin(' + self.current_expression

    def trig_cosine(self):
        self.current_expression =  'cos(' + self.current_expression

    def trig_tangent(self):
        self.current_expression =  'tan(' + self.current_expression

    def squared(self):
        self.current_expression = self. current_expression + '²'

    def sqrt(self):
        self.current_expression = 'sqrt(' + self.current_expression

    def cubed(self):
        self.current_expression = self. current_expression + '³'

    def perm(self):
        self.current_expression = self.current_expression + 'P'

    def comb(self):
        self.current_expression = self.current_expression + 'C'

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""

    def delete(self):
        self.current_expression = str(self.current_expression[:-1])

    def answer(self):
        self.answer = str(self.total_expression)
        self.current_expression = self.current_expression + self.answer

    def exp_function(self):
        self.current_expression = self.current_expression + 'E'

    def evaluate(self):
        self.total_expression += self.current_expression

        if '²' in self.total_expression or '³' in self.total_expression or 'E' in self.total_expression:
            self.current_expression = str(eval(self.total_expression.replace('²', '**2').replace('³', '**3').replace('E','*10**')))
        elif 'P' in self.total_expression:
            n,r = self.current_expression.split('P')
            n,r = int(n), int(r)
            if n >= r >= 0:
                self.current_expression = str(eval(f'math.factorial({n})' + '//' + f'math.factorial({n}-{r})'))
            else:
                self.current_expression = 'Math Error'
        elif 'C' in self.total_expression:
            n,r = self.current_expression.split('C')
            n,r = int(n), int(r)
            if 0 <= r <= n:
                self.current_expression = str(eval(f'math.factorial({n})' + '//' + f'math.factorial({r})' + '//' + f'math.factorial({n}-{r})'))
            else:
                self.current_expression = 'Math Error'
        else:
            try:
                self.current_expression = str(eval(self.total_expression))
                self.total_expression = ""
            except Exception as e:
                self.current_expression = "Error"



