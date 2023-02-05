from math import floor, sqrt
from scipy.special import gammainc
from fractions import Fraction


def test (sequence,n,M=32):

    # Compute number of blocks M = block size. N=num of blocks
    # N = floor(n/M)
    # miniumum block size 20 bits, most blocks 100
    # fieldnames = ['number','chisq','p-value', 'success']

    N = int(floor(n/M))

    if N > 99:
        N= 99
        M = int(floor(n/N))

    if n < 100 :
        # Too little data for test. Input of length at least 100 bits required
        return [0.0,0,0,False]
    
    num_of_blocks = N

    block_size = M

    proportions = list()

    for i in range(num_of_blocks):
        block = sequence[i*(block_size):((i+1)*(block_size))]

        ones = block.count('1')
        zeroes = block.count('0')
        proportions.append(Fraction(ones,block_size))
    
    chisq = 0.0

    for prop in proportions:
        chisq += 4.0*block_size*((prop - Fraction(1,2))**2)
    
    p = gammainc((num_of_blocks/2.0),float(chisq)/2.0) # p-value
    success = (p>= 0.01) 

    return [chisq ,p , success]
        



        



