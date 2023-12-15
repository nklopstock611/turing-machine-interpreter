R '2'
P
? '#' label-go-to-x ; means, if on current position there is a '#' char...
R '3'
W '&'
P
HALT

label-go-to-x:
R
W '$'
P
C label-go-to-x