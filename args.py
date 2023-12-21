def help():
    help_text = """
    Main instructions:

    - L [n] := (Left) Move one position to the left. Optional param indicates how many "lefts" it moves.

    - R [n] := (Right) Move one position to the right. Optional param indicates how many "rights" it moves.

    - W char := (Write) char on current position.

    - P := (Print) (or, read) char on current position.

    - HALT := Ends a main block. Every main block has to end with HALT.

    Every program consists of one main block and an optional *label* block. The main block is where the code that will execute goes. The label block is where all the labels and its instructions go.
    
    Extra instructions:

    - C label := (Continue) execution from label.

    - ? char label := If on current position there is char, go to label.

    - S := (Save)s a char.

    - G := (Get)s the saved char.

    - HC := (Head Currently) Prints the current position of the head.

    - FT := (Full Tape) Prints the complete tape.

    - ; := Comment. Everything after ; is ignored.

    Visit the repo for the full documentation.
    """

    return help_text

def string(string):
    program = []
    for each_char in string:
        program.append('W')
        program.append(each_char)
        program.append('R')

    return program
