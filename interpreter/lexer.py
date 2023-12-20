def ignore_comments(line):
    for each_char in line:
        if each_char == ';':
            return line[:line.index(';') - 1]
        
    return line

def ignore_whitespaces(line):
    return line.replace(' ', '')

def ignore(line):
    line = ignore_comments(line)
    line = ignore_whitespaces(line)
    return line

def halt_label_index_difference(program_lines: list):
    try:
        index_halt = 0
        index_label = 0
        for line in program_lines:
            if line != '':
                if line[-1] == ':':
                    break
                index_label += 1
                if line == 'HALT':
                    break
                index_halt += 1

        return index_halt + 1 == index_label
    except:
        raise SyntaxError('Halting Error! - Seems you forgot to put a HALT instruction at the end of the main block.')

def program_array(program_filepath):
    # reads file lines
    program_lines = []
    with open(program_filepath, 'r') as f:
        program_lines = [line.strip() for line in f.readlines()]

    program = []
    token_counter = 0
    label_tracker = {}
    label_call_tracker = {}
    for line_number, line in enumerate(program_lines, 1):
        line = ignore(line)
        
        # check for empty line
        if line == '':
            continue

        instruction = line[0]

        # check for label
        if line[-1] == ':':
            label_tracker[line[:-1]] = token_counter - 1 # saves the index of the label
            continue

        if instruction == 'L' or instruction == 'R':
            # L 2 || R 'A'
            program.append(instruction)
            token_counter += 1
            if len(line) > 1:       

                if (line[1] == "'" or line[-1] == "'") and line.count("'") != 2:
                    raise SyntaxError(f"Error at line {line_number} - Seems you forgot a \' on L or R instruction.")

                if line[1] == "'":
                    program.append(line[2:-1])
                    program.append('char')
                    token_counter += 2
                else:
                    if (line[1:].isdigit() == False):
                        raise SyntaxError(f"Error at line {line_number} - L's or R's optional param must be a number or a char.")
                    
                    program.append(line[1:])
                    program.append('times')
                    token_counter += 2
            else:
                program.append('1')
                program.append('times')
                token_counter += 2

        elif instruction == 'W':
            # W '$'
            program.append(instruction)
            token_counter += 1
            if line[1] == "'":
                program.append(line[2:-1])
                token_counter += 1
            elif line[1] == 'G':
                # W G
                program.append(line[1])
                token_counter += 1
            else:
                raise SyntaxError(f"Error at line {line_number} - W's param must be a char or an assigned G instruction.")

        elif instruction == 'C':
            # C label-go-to-x
            program.append(instruction)
            
            if (line[1:] not in label_tracker):
                raise SyntaxError(f"Error at line {line_number} - Label {line[1:]} not found.")
            
            program.append(line[1:])
            token_counter += 2

        elif instruction == '?':
            # ? '$' label-go-to-x
            program.append(instruction)
            program.append(line[2:3])
            program.append(line[4:])
            token_counter += 3
            label_call_tracker[line[4:]] = token_counter - 1

        elif line == 'HC' or line == 'P' or line == 'S' or line == 'FT' or line == 'HALT':
            program.append(line)
            token_counter += 1
            continue

        else:
            raise SyntaxError(f"Error at line {line_number} - Not a valid instruction.")

    if halt_label_index_difference(program_lines) == False:
        raise SyntaxError('Halting Error! - Seems you forgot to put a HALT instruction at the end of the main block.')

    return (program, label_tracker, label_call_tracker)







