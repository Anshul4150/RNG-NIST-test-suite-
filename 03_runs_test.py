from scipy.special import erf
from math import sqrt
def test(sequence ,n ):
    ones = sequence.count('1')
    zeroes = sequence.count('0')
    prop = float(ones)/float(n)

    tau = 2.0/sqrt(n)
    vobs = 0.0

    if abs(prop-0.5) > tau :
        p = 0
    
    else:
        vobs = 1.0

        for i in range(n-1):
            if sequence[i] != sequence[i+1] :
                vobs +=1.0
        p = erf(abs(vobs - (2.0*n*prop*(1.0-prop)))/(2.0*sqrt(2.0*n)*prop*(1-prop) ))
    success = (p>=0.01)

    return [zeroes,ones,prop,vobs,p,success]