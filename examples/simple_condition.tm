HC
R 2
HC
P
? '#' label-go-to-x ; means, if there is a '#' char on current position, go to label-go-to-x
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
C label-go-to-x ; means, continue execution from where label-go-to-x was called