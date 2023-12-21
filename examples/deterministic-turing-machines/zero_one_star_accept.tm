; Deterministic Turing Machine that recognizes the language
; L = (01)*

; writes word to evaluate
W '0'
R
W '1'
R
W '0'
R
W '1'
FT

; evaluation starts
? '#' accept
L 3
? '0' evaluation

HALT

evaluation:
R
? '1' q1
C evaluation

q1:
R
? '0' q2
? '#' accept
C evaluation

q2:
R
? '1' q1
C evaluation

accept:
W 'A'
C evaluation