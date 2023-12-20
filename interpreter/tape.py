class Tape:

    def __init__(self, size, char):
        self.tape = [char for _ in range(size)]
        self.pointer = 0
        self.g = '#'

    def read(self):
        return self.tape[self.pointer]
    
    def write(self, value):
        self.tape[self.pointer] = value
    
    def left(self):
        self.pointer -= 1

    def left_scan(self, char):
        found = False
        for _ in reversed(range(0, self.pointer)):
            if self.tape[self.pointer] == char:
                found = True
                break

            self.left()

        if found == False:
            raise NameError(f"Error: Character '{char}' not found in tape when doing a left scan")

    def right(self):
        self.pointer += 1

    def right_scan(self, char):
        found = False
        for _ in range(self.pointer, len(self.tape)):
            if self.tape[self.pointer] == char:
                found = True
                break

            self.right()

        if found == False:
            raise NameError(f"Error: Character '{char}' not found in tape when doing a right scan")

    def __str__(self):
        return str(self.tape)
    
    def get_pointer(self):
        return self.pointer
    
    def set_g(self):
        self.g = self.tape[self.pointer]

    def get_g(self):
        if self.g == '#':
            raise NameError(f"Error: G is not set")
        return self.g
