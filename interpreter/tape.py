class Tape:

    def __init__(self, size):
        self.tape = ['#' for _ in range(size)]
        self.pointer = 0
        self.g = '#'

    def read(self):
        return self.tape[self.pointer]
    
    def write(self, value):
        self.tape[self.pointer] = value
    
    def left(self):
        self.pointer -= 1

    def right(self):
        self.pointer += 1

    def __str__(self):
        return str(self.tape)
    
    def get_pointer(self):
        return self.pointer
    
    def set_g(self):
        self.g = self.tape[self.pointer]

    def get_g(self):
        return self.g
