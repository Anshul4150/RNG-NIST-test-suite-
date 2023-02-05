
import numpy as np
from math import sqrt , log
from scipy.special import erf

def test(sequence,n):

    T = sqrt(log(1.0/0.05)*n)

    N0 = 0.95*n/2.0
    
    write_array = [0.0,0.0,0.0,0.0]

    ts = list()

    for i in range(n):
        if sequence[i] == "1":
            ts.append(1)
        else:
            ts.append(-1)
    
    ts_np = np.array(ts)

    fs = np.fft.fft(ts_np)
    mags = abs(fs[:int(n/2)])

    N1 = 0.0

    for mag in mags :
        if mag <T :
            N1 +=1.0
    d = (N1-N0)/sqrt((n*0.95*0.05)/4)

    p = erf(abs(d)/sqrt(2))

    success = (p>=0.01)
    return [N0,N1,d,p,success] 
     









