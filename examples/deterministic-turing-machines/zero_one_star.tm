; Deterministic Turing Machine that recognizes the language
; L = (01)*
; examples accept: "0101", ""
; examples reject: "010", "0"

; writes word to evaluate
; you can write it in the main program, like this:
; W '0'
; R
; W '1'
; R
; W '0'
; R
; W '1'
; FT
; L 3
; or use the argument on the terimal --string "0101"

; evaluation starts
? '#' accept
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