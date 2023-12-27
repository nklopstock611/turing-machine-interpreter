; Deterministic Turing Machine that recognizes the language of all strings over {x, y, z, C} in the form wCw,
; where w is any string containing only x, y, and z. 
; examples accept: "#xyzCxyz", "#xyCxy", "#C", "#xyCyx"
; examples reject: "#xyC", "#xyCyxz", "#xyCxyCxy", "#xyCxyCyx"

; evaluation starts
R

; two possible starting transitions

? '$' q1

? 'x' q2
? 'y' q2
? 'z' q2

? 'C' q5

? '#' halt ; end of string
HALT

halt:
TO halt

q1:
R
? '$' q1
? 'C' q5

S ; G is set to what ever's on the current position of the tape
? 'x' q2
? 'y' q2
? 'z' q2
TO halt

q2:
S
W '$'
R 'C'
R !'$'
? G q3
? !G q4
TO halt

q3:
W '$'
L '#'
R
? '$' q1
TO halt

q4:
TO halt

q5:
R !'$'
? '#' accept
TO q4

accept:
W 'A'
TO halt