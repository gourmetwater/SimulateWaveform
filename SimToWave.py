import numpy as np
import sys
import wavio
from csvsifter import siftcsv

filename = sys.argv[1]
data, duration = siftcsv(dataname=filename)
base = np.copy(data)

rate = base.size/duration
#T = int(3/duration)*duration
T = 3
for n in range(1,(int(3/duration)+1)):
    data = np.concatenate((data,base),axis = 0)

wavio.write("Vout.wav",data,rate,sampwidth = T)