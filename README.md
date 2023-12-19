# turing-machine-interpreter
Interpreter for a little Turing Machine like language.

It consists of a long tape and a head that can move to the left and to the right, and can write and read characters.

## Instructions
### Main instructions:
`L [n]` := (Left) Move one position to the left. Optional param indicates how many "lefts" it moves.

`R [n]` := (Right) Move one position to the right. Optional param indicates how many "rights" it moves.

`W char` := (Write) char on current position.

`P` := (Print) (or, read) char on current position.

`HALT` := Ends a *main* block. Every *main* block has to end with `HALT`.

Every program consists of one *main* block and an optional *label* block. The *main* block is where the code that will execute goes. The *label* block is where all the labels and its instructions go.

```
; main block:
R 2
? '#' label-main-block
HALT

; label block:
label-main-block:
W '$'
P
C label-main-block
```

Be sure to write the *main* block of code first and then the labels, because the interpreter reads the code from top to bottom.

It's important to note that after each complete instruction, there must be a new line.

### Extra instructions:
`C label` := (Continue) execution from label.

`? char label` := If on current position there is char, go to label.

`S` := (Save)s a char.

`G` := (Get)s the saved char.

`HC` := (Head Currently) Prints the current position of the head.

`FT` := (Full Tape) Prints the complete tape.

`;` := Comment. Everything after `;` is ignored.

### For a more modern feel
#### Variables:
Use the `S` instruction to save the char on the current position of the head. You can later get that char using the `G` instruction.

Example:
```
W '$' ; writes '$' on 0
S
R 4
W G ; writes '$' on 4
P
HALT 
```

#### Conditions:
Use the instruction `? char label` to indicate conditions. Use a label to send the execution to that line, depending on the char condition.

Also, use the instruction `C label` to continue the execution from that label.

Example:
```
R 2
P
? '#' label-go-to-x ; means, if on current position there is a '#' char, go to label-go-to-x
R 3
W '&'
P
HALT

label-go-to-x:
R
W '$'
P
C label-go-to-x ; means, continue from label-go-to-x
```

#### Loops (move until):
Use the `L` or `R` instruction with a char (like so `L '$'`) to indicate that the head has to move to the left or to the right until it finds that char.

Example:
```
HC ; starts at 0
R 4
HC ; moves to 4
W '$' ; writes '$' on 4
P ; reads '$' on 4
L 2
HC ; moves to 2
R '$'
HC ; moves to 4, because the first '$' to the right was on 4
P ; reads '$' on 4
HALT
```

