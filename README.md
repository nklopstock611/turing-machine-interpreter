# turing-machine-interpreter
Little interpreter for a Turing Machine like language.

It consists of a long tape and a read-head that can move to the left and to the right, and can write and read characters.

## Instructions
`L ['n']` := Move one position to the left. Optional param indicates how many "lefts" it moves.

`R ['n']` := Move one position to the right. Optional param indicates how many "rights" it moves.

`W char` := Write char on current position.

`P` := Print (or, read) char on current position.

`HALT` := End a label block or the full program. Every label block and every program has to end with `HALT`.

### For a more modern feel
#### Conditions:
Use the instruction `? char label` to indicate conditions. Use a label to send the execution to that line, depending on the char condition.

Example:
```
label-go-to-x:
R
W '$'
HALT

R '2'
P
? '#' label-go-to-x // means, if on current position there is a '#' char...
HALT
```

