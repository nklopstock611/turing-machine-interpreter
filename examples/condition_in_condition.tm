HC ; 0
R 2
HC ; 2
P ; '#'
? '#' label-first-condition
FT

HALT

label-first-condition:
W '$'
P ; '$'
S ; saves '$'
L
HC ; 1
W G
P ; '$'
? '$' label-second-condition
C label-first-condition

label-second-condition:
W '&'
P ; '&'
C label-second-condition