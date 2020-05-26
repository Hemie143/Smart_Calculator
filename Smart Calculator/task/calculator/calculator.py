# write your code here

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
