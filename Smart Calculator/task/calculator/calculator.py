# write your code here
# https://web.archive.org/web/20190618091844/http://interactivepython.org:80/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
# https://stackoverflow.com/questions/41164797/method-to-convert-infix-to-reverse-polish-notationpostfix


class SmartCalc():

    def __init__(self):
        self.vars = {}
        self.cmd = None

    def assign_var(self):
        try:
            var, value = self.cmd.split('=')
            var = var.strip()
            value = value.strip()
            if value.isalpha():
                self.vars[var] = self.get_var(value.strip())
            else:
                self.vars[var] = int(value.strip())
        except:
            print('Invalid assignment')

    def get_var(self, var_name):
        var_name = var_name.strip()
        if var_name in self.vars:
            return self.vars[var_name]
        else:
            print('Unknown variable')
        return

    def toPostfix(infix):
        stack = []
        postfix = ''

        for c in infix:
            if isOperand(c):
                postfix += c
            else:
                if isLeftParenthesis(c):
                    stack.append(c)
                elif isRightParenthesis(c):
                    operator = stack.pop()
                    while not isLeftParenthesis(operator):
                        postfix += operator
                        operator = stack.pop()
                else:
                    while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):
                        postfix += stack.pop()
                    stack.append(c)

        while (not isEmpty(stack)):
            postfix += stack.pop()
        return postfix

    def toRpn(infixStr):
        # divide string into tokens, and reverse so I can get them in order with pop()
        tokens = re.split(r' *([\+\-\*\^/]) *', infixStr)
        tokens = [t for t in reversed(tokens) if t != '']
        precs = {'+': 0, '-': 0, '/': 1, '*': 1, '^': 2}

        # convert infix expression tokens to RPN, processing only
        # operators above a given precedence
        def toRpn2(tokens, minprec):
            rpn = tokens.pop()
            while len(tokens) > 0:
                prec = precs[tokens[-1]]
                if prec < minprec:
                    break
                op = tokens.pop()

                # get the argument on the operator's right
                # this will go to the end, or stop at an operator
                # with precedence <= prec
                arg2 = toRpn2(tokens, prec + 1)
                rpn += " " + arg2 + " " + op
            return rpn

        return toRpn2(tokens, 0)

    def compute_cmd(self):
        elements = self.cmd.split()
        for i, e in enumerate(elements):
            if e.isalpha():
                elements[i] = str(self.vars[e])
        compute_line = ' '.join(elements)
        try:
            result = eval(compute_line)
        except:
            print("Invalid expression")
        else:
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
