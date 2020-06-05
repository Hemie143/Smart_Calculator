# write your code here
from collections import deque
import re


class SmartCalc:
    precs = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

    def __init__(self):
        self.vars = {}
        self.cmd = None
        self.stack = deque()

    def assign_var(self):
        try:
            var, value = self.cmd.split('=')
            var = var.strip()
            value = value.strip()
            if value.isalpha():
                self.vars[var] = self.get_var(value.strip())
            else:
                self.vars[var] = value.strip()
        except:
            print('Invalid assignment')

    def get_var(self, var_name):
        var_name = var_name.strip()
        if var_name in self.vars:
            return self.vars[var_name]
        else:
            print('Unknown variable')
        return

    @staticmethod
    def clean_operator(ops):
        if ops and all([o == '+' for o in ops]):
            return '+'
        elif ops and all([o == '-' for o in ops]):
            if len(ops) % 2 == 0:
                return '+'
            else:
                return '-'
        elif ops and ops[0] in ['*', '/', '^']:
            return ops[0]
        elif ops:
            print('Unknown operators ?')
            return

    def clean_up_chain(self, chars):
        # Clean up the operators
        chars = [c for c in chars if c != '']
        result = []
        current_ops = []
        for i, c in enumerate(chars):
            if c.isnumeric() or c in '()':
                op = self.clean_operator(current_ops)
                if op:
                    result.append(op)
                result.append(c)
                current_ops = []
            elif c in self.precs:
                current_ops.append(c)
            elif c in self.vars:
                op = self.clean_operator(current_ops)
                if op:
                    result.append(op)
                result.append(self.vars[c])
                current_ops = []
            else:
                print('Error parsing input')
        return result

    def convert_to_rpn(self):
        # divide string into tokens, and reverse so I can get them in order with pop()
        chars = re.split(r' *([\+\-\*\^/\(\)]) *', self.cmd)
        chars = self.clean_up_chain(chars)
        if chars.count('(') != chars.count(')'):
            return 'Invalid expression'
        tokens = deque()
        tokens.extend(chars)
        self.stack = deque()
        ops_stack = deque()
        while len(tokens) > 0:
            token = tokens.popleft()
            if token.isnumeric():
                self.stack.append(token)
            # check if a known function
            elif token in self.precs:
                # top_op = ops_stack[-1]
                while (len(ops_stack) > 0 and (ops_stack[-1] in self.precs) and (
                        (self.precs[ops_stack[-1]] > self.precs[token])
                        or (self.precs[ops_stack[-1]] == self.precs[token] and token in '+-*/'))
                       and (ops_stack[-1] != '(')):
                    self.stack.append(ops_stack.pop())
                ops_stack.append(token)
            elif token == '(':
                ops_stack.append(token)
            elif token == ')':
                while ops_stack[-1] != '(':
                    self.stack.append(ops_stack.pop())
                if ops_stack[-1] == '(':
                    ops_stack.pop()
        while len(ops_stack) > 0:
            self.stack.append(ops_stack.pop())
        return

    def eval_stack(self):
        calc_stack = deque()
        while len(self.stack) > 0:
            element = self.stack.popleft()
            if element.isnumeric():
                calc_stack.append(element)
            elif element.isalpha():
                # TEST ?
                calc_stack.append(self.get_var(element))
            elif element in self.precs:
                # pop twice and perform operation
                # push result to stack
                y = float(calc_stack.pop())
                x = float(calc_stack.pop())
                if element == '+':
                    calc_stack.append(x + y)
                elif element == '-':
                    calc_stack.append(x - y)
                elif element == '*':
                    calc_stack.append(x * y)
                elif element == '/':
                    calc_stack.append(x / y)
                elif element == '^':
                    calc_stack.append(x ^ y)
        result = calc_stack.popleft()
        return int(result)

    def compute_cmd(self):
        elements = self.cmd.split()
        msg = self.convert_to_rpn()
        if msg:
            print(msg)
            return
        result = self.eval_stack()
        print(result)
        return

    def eval_cmd(self):
        if '+' in self.cmd or '-' in self.cmd:
            self.compute_cmd()
        elif '=' in self.cmd:
            self.assign_var()
        elif self.cmd.isalpha():
            print(self.get_var(self.cmd))

    def run(self):
        while True:
            self.cmd = input()
            if not self.cmd:
                continue
            elif self.cmd == '/help':
                print('The program calculates the sum of numbers')
            elif self.cmd == '/exit':
                print('Bye!')
                exit()
            elif self.cmd.startswith('/'):
                print('Unknown command')
                continue
            self.eval_cmd()


calc = SmartCalc()
calc.run()
