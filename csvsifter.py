import numpy as np

#data = np.loadtxt(dataname, delimiter=",") NOPE
def siftcsv(dataname):
    data = np.genfromtxt(dataname,delimiter=",")
    samplewidth = data[-1,0] - data[1,0]
    data = data[:,1]
    data = data[~np.isnan(data)]
    return data, samplewidth

