import pandas as pd
import numpy as np
from scipy.spatial import distance

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))


data = np.genfromtxt("E:/Swarm Intelligence/Tugas 1/Swarm016.txt",usecols = range(1,3));
data = np.array(data)
#X.columns = ['X', 'Y']
euc = np.zeros((data.shape[0],data.shape[0]))
for ii in range(data.shape[0]):
    for yy in range(data.shape[0]):
        euc[ii,yy] = dist(data[ii,:],data[yy,:])
#print(euc[1,2])

jumlahpartikel = 100
position = np.random.uniform(low=0, high=1, size=((jumlahpartikel, data.shape[0])))
positionBest =position
jarak = np.zeros((1,jumlahpartikel))                                                  #jarak sebagai fitness
jarakBest = np.zeros((1,jumlahpartikel))
velocity = np.zeros((jumlahpartikel,data.shape[0]))
velocityMax = 100
velocityMin = -100
kognitif = 2
sosial = 5
tempKonvergen = 0                                                                     #interval 0 hingga 1
urutankota = np.argsort(position)
urutankota = np.column_stack([urutankota,urutankota[:,0]])
#print(position)
for ii in range(data.shape[0]):
#   print(ii , ' : ' ,euc[urutankota[:,ii],urutankota[:,ii+1]])                       #mengambil jarak kota ke ii dengan kota ke ii+1
    jarak =  np.sum([jarak,euc[urutankota[:,ii],urutankota[:,ii+1]]], axis=0)         #menghitung jarak urutan tiap kota
#print(jarakBest)
jarakBest = jarak
jarakTemp = jarak
perulangan = 0
while tempKonvergen<5:
    sortJarak = np.argsort(jarak)
    for ii in range(jumlahpartikel):
        velocity[ii,:] = velocity[ii,:] + kognitif*np.random.random()*(positionBest[ii,:]-position[ii,:])+sosial*np.random.random()*(positionBest[sortJarak[0,0],:]-position[ii,:])
    velocity[velocity>velocityMax] = velocityMax
    velocity[velocity<velocityMin] = velocityMin
    position = position + velocity

    urutankota = np.argsort(position)
    urutankota = np.column_stack([urutankota, urutankota[:, 0]])
    jarak = np.zeros((1, jumlahpartikel))
    for ii in range(data.shape[0]):
        jarak = np.sum([jarak, euc[urutankota[:, ii], urutankota[:, ii + 1]]], axis=0)  # menghitung jarak urutan tiap kota
    cekJarakBest = np.any(jarak-jarakBest < 0, axis=0)
    #print(urutankota[1, :])
    #print(velocity[1,:])
    #print(jarak[0,1])

    for ii in range(jumlahpartikel):
        if(cekJarakBest[ii]):
            jarakBest[0,ii] = jarak[0,ii]
            positionBest[ii,:] = position[ii,:]
    if np.sum(jarak - jarakTemp)<=0:
        tempKonvergen = tempKonvergen + 1
    else:
        tempKonvergen = 0
    jarakTemp = jarak
    perulangan = perulangan + 1

print(perulangan)
print(jarakBest)
#print(urutankota)
#print(data.shape[0])
#print(euc)


#https://stackoverflow.com/questions/25013792/how-to-read-a-dataset-from-a-txt-file-in-python
