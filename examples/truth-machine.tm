? '#' repeat
? '1' truth
? '0' halt
HALT

repeat:
TO repeat

truth:
R
W '1'
TO repeat

halt:
TO halt
