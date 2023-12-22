; Deterministic Turing Machine that recognizes the language that follows the regular expression (01)*
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

; accepts empty string
? '#' accept

? '0' q2 ; first transition

? '#' halt ; end of string
HALT

halt:
TO halt

q1:
R
? '0' q2
? '#' accept
TO halt

q2:
R
? '1' q1
TO halt

accept:
W 'A'
TO halt
