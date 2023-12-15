import sys

import tape as t
import lexer as l
# import parser as p

program_filepath = sys.argv[1]

pointer = 0
program, label_tracker, label_call_tracker = l.lexer(program_filepath)
tape = t.Tape(256)

while program[pointer] != 'HALT':
    instruction = program[pointer]

    if instruction == 'L':
        times = program[pointer + 1]
        if times.isdigit():
            for _ in range(int(times)):
                tape.left()
        else:
            tape.left()

    elif instruction == 'R':
        times = program[pointer + 1]
        if times.isdigit():
            for _ in range(int(times)):
                tape.right()
        else:
            tape.right()

    elif instruction == 'W':
        tape.write(program[pointer + 1])

    elif instruction == 'P':
        print(tape.read())

    elif instruction == '?':
        if tape.read() == program[pointer + 1]:
            pointer = label_tracker[program[pointer + 2]]
        else:
            pointer += 1

    elif instruction == 'C':
        pointer = label_call_tracker[program[pointer + 1]]
        
    pointer += 1

