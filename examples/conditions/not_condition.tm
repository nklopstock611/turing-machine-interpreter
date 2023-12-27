S ; G is set to '#'
W '$'
? !'#' label-one
HALT

label-one:
W G
R
W '$'
? !G label-two
TO label-one

label-two:
W '#'
TO label-two