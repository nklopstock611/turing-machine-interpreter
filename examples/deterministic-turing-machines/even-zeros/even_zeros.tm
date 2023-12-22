; Deterministic Turing Machine that recognizes the language of all strings over {0,1} that contain an even number of 0s.
; examples accept: "1001", ""
; examples reject: "0100", "0"

; writes word to evaluate
; you can write it in the main program, like this:
; W '1'
; R
; W '0'
; R
; W '0'
; R
; W '1'
; FT
; L 3
; or use the argument on the terimal --string "1001"

; evaluation starts

; accepts empty string
? '#' accept

; two possible starting transitions
? '1' q1
? '0' q2

? '#' halt ; end of string
HALT

halt:
TO halt

q1:
R
? '0' q2
? '1' q1
? '#' accept
TO halt

q2:
R
? '1' q2
? '0' q1
TO halt

accept:
W 'A'
TO halt