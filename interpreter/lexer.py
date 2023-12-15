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

def lexer(program_filepath):
    # reads file lines
    program_lines = []
    with open(program_filepath, 'r') as f:
        program_lines = [line.strip() for line in f.readlines()]

    program = []
    token_counter = 0
    label_tracker = {}
    label_call_tracker = {}
    for line in program_lines:

        # check for empty line
        if line == '':
            continue

        # check for label
        if line[-1] == ':':
            label_tracker[line[:-1]] = token_counter # saves the index of the label
            continue

        token_counter += 1

        # check for instruction
        if line[0] == 'L' or line[0] == 'R':
            # L '2' || R '2'
            line = ignore(line)
            program.append(line[0])
            if len(line) > 1:
                # program.append(line[1])
                program.append(line[2:-1])
            token_counter += 1

        elif line[0] == 'W':
            # W '$'
            line = ignore(line)
            program.append(line[0])
            program.append(line[2:-1])
            token_counter += 1

        elif line == 'P':
            # P
            line = ignore(line)
            program.append(line[0])

        elif line[0] == '?':
            # ? '$' label-go-to-x
            line = ignore(line)
            program.append(line[0])
            program.append(line[2:3])
            program.append(line[4:])
            label_call_tracker[line[4:]] = token_counter
            token_counter += 1

        elif line[0] == 'C':
            line = ignore(line)
            program.append(line[0])
            program.append(line[1:])

        elif line == 'HC':
            line = ignore(line)
            program.append(line)

        elif line == 'FT':
            line = ignore(line)
            program.append(line)

        elif line == 'HALT':
            line = ignore_comments(line)
            program.append(line)

    return (program, label_tracker, label_call_tracker)
