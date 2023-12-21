HC ; 0
R 4
HC ; 4
W '$'
P ; '$'
R
HC ; 5
W '&'
P ; '&'

L 4
HC ; 1

R '$'
HC ; 4
? '$' label-usd-sign

R '&'
HC ; 5
? '&' label-ampersand

HALT

label-usd-sign:
W '#'
P ; '#'
L 4
HC ; 0
TO label-usd-sign

label-ampersand:
W '#'
P ; '#'
L 4
HC ; 1
TO label-ampersand