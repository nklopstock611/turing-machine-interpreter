; Deterministic Turing Machine that recognizes the language of all strings over {0,1} that contain an even number of 0s.
; examples accept: "1001", ""
; examples reject: "0100", "0"

; evaluation starts
? '#' accept
? '1' q1
? '0' q2

? '#' end

HALT

end:
TO end

q1:
R
? '0' q2
? '1' q1
? '#' accept
TO end

q2:
R
? '1' q2
? '0' q1
TO end

accept:
W 'A'
TO end