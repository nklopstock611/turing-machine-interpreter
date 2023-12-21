; Deterministic Turing Machine that recognizes the language
; L = (01)*

; writes word to evaluate
W '0'
R
W '1'
R
W '0'
FT

; evaluation starts
L 2
? '0' evaluation

HALT

evaluation:
R
? '1' q1

q1:
R
? '0' q2
? '#' accept

q2:
R
? '1' q1
? '#' reject

accept:
W 'A'
C evaluation

reject:
W 'R'
C evaluation