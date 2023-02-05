from math import sqrt
from scipy.special import erf

def test(sequence,n):
    ones = sequence.count('1')
    zeroes = sequence.count('0')

    s = abs(ones-zeroes)

    p = erf(float(s)/(sqrt(float(n)) * sqrt(2.0)))

    success = (p>= 0.01 )

    return [zeroes , ones , s , p , success]
