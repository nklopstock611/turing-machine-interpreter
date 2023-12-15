HC
R 2
HC
P
? '#' label-go-to-x ; means, if on current position there is a '#' char...
R 3
HC
W '&'
P
HALT

label-go-to-x:
R
HC
W '$'
P
C label-go-to-x