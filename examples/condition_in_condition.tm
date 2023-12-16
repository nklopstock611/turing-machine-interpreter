HC
R 2
HC
P
? '#' label-first-condition
FT

HALT

label-first-condition:
W '$'
P
S
L
HC
W G
P
? '$' label-second-condition
C label-first-condition

label-second-condition:
W '&'
P
C label-second-condition