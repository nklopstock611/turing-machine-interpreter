import sys

import interpreter.tape as t
import interpreter.lexer as l

def run(tape: t.Tape, program: list, pointer: int):
    while program[pointer] != 'HALT':
        instruction = program[pointer]

        if instruction == 'L':
            if program[pointer + 2] == 'times':
                times = program[pointer + 1]
                if times.isdigit():
                    for _ in range(int(times)):
                        tape.left()
                else:
                    tape.left()
            elif program[pointer + 2] == 'char':
                char = program[pointer + 1]
                tape.left_scan(char)

        elif instruction == 'R':
            if program[pointer + 2] == 'times':
                times = program[pointer + 1]
                if times.isdigit():
                    for _ in range(int(times)):
                        tape.right()
                else:
                    tape.right()
            elif program[pointer + 2] == 'char':
                char = program[pointer + 1]
                tape.right_scan(char)

        elif instruction == 'W':
            if program[pointer + 1] == 'G':
                tape.write(tape.get_g())
            else:
                tape.write(program[pointer + 1])

        elif instruction == 'P':
            print(tape.read())

        elif instruction == 'C':
            pointer = label_call_tracker[program[pointer + 1]]

        elif instruction == 'S':
            tape.set_g()

        elif instruction == '?':
            if tape.read() == program[pointer + 1]:
                pointer = label_tracker[program[pointer + 2]]
                print(program[pointer])
            else:
                pointer += 1

        elif instruction == 'HC':
            print(tape.get_pointer())

        elif instruction == 'FT':
            print(tape.__str__())
            
        pointer += 1

if __name__ == '__main__':
    program_filepath = sys.argv[1]
    # program_filepath = 'examples/simple_condition.tm'

    pointer = 0
    tape = t.Tape(256)
    try:
        program, label_tracker, label_call_tracker = l.program_array(program_filepath)

        print(program)
        print(label_tracker)
        print(label_call_tracker)
        run(tape, program, pointer)
    except Exception as e:
        print(e)