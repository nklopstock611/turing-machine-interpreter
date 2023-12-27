import sys
import argparse
import args as a

from interpreter.tape import Tape
import interpreter.lexer as l

def run(tape: Tape, program: list, label_tracker: dict, label_call_tracker: dict, pointer: int, show_full_tape: bool = False):
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
            elif program[pointer + 2] == 'not_char':
                char = program[pointer + 1]
                tape.left_scan_not(char)

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
            elif program[pointer + 2] == 'not_char':
                char = program[pointer + 1]
                tape.right_scan_not(char)

        elif instruction == 'W':
            if program[pointer + 2] == 'G':
                tape.write(tape.get_g())
            else:
                tape.write(program[pointer + 1])

        elif instruction == 'P':
            print(tape.read())

        elif instruction == 'C':
            c_filepath = program[pointer + 1]
            c_program, c_label_tracker, c_label_call_tracker = l.program_array(c_filepath)
            run(tape, c_program, c_label_tracker, c_label_call_tracker, 0, show_full_tape)

        elif instruction == 'TO':
            pointer = label_call_tracker[program[pointer + 1]]

        elif instruction == 'S':
            tape.set_g()

        elif instruction == '?':                
            if program[pointer + 2] == 'G':
                if tape.read() == tape.get_g():
                    pointer = label_tracker[program[pointer + 3]]
                else:
                    pointer += 1
            elif program[pointer + 2] == 'not_char':
                if tape.read() != program[pointer + 1]:
                    pointer = label_tracker[program[pointer + 3]]
                else:
                    pointer += 1
            elif program[pointer + 2] == 'not_g':
                if tape.read() != tape.get_g():
                    pointer = label_tracker[program[pointer + 3]]
                else:
                    pointer += 1
            else:
                if tape.read() == program[pointer + 1]:
                    pointer = label_tracker[program[pointer + 3]]
                else:
                    pointer += 1

        elif instruction == 'HC':
            print(tape.get_pointer())

        elif instruction == 'FT':
            print(tape.__str__())
            
        if show_full_tape and instruction in {'L', 'R', 'W'}:
            tape.print_ft_on_current_position()
        
        pointer += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('program_filepath', help='The path to the program file')

    # optional args
    parser.add_argument('--h', action='store_true', help='Prints help message')
    parser.add_argument('--tape-size', type=int, default=256, help='The size of the tape')
    parser.add_argument('--initial-state-char', type=str, default='#', help='The initial state char of the tape')
    parser.add_argument('--show-full-tape', action='store_true', help='Shows the full tape (and the head position) after each intruction')
    parser.add_argument('--string', nargs='?', const='', help='The string that will be evaluated')

    args = parser.parse_args()

    if args.h:
        print(a.help())
        sys.exit(0)

    program_filepath = args.program_filepath

    pointer = 0
    tape = Tape(args.tape_size, args.initial_state_char)

    try:

        if program_filepath[-3:] != '.tm':
            raise FileNotFoundError(f"Error: Program file must have the .tm extension")
        # program_filepath = 'examples/simple-instructions/simple_tm_call.tm'

        program, label_tracker, label_call_tracker = l.program_array(program_filepath)

        if args.string:
            tape.string_to_evaluate(args.string)

        run(tape, program, label_tracker, label_call_tracker, pointer, args.show_full_tape)

        if args.show_full_tape:
            print(tape.__str__())
            
    except SyntaxError as e:
        print(e)
    except NameError as e:
        print(e)
    except FileNotFoundError as e:
        print('Error: File not found.')
        print(e)
    except IndexError as e:
        print(f"Error: The tape is not long enough to execute the program.")