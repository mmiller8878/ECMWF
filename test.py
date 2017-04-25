import pygrib
import csv
import pandas as pd
import numpy as np
import os

grbs = pygrib.open('/home/ecmwf/D1D03160000031718001')
#grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
for grb in grbs:
    print (grb)

grbz = pygrib.open('/home/ecmwf/D1E03270000041100001')
#for grb in grbz:
#    print (grb)

#for dataset in grbz:
    #print(dataset['parameterUnits'],dataset['timeRangeIndicator'],dataset['P1'], dataset['P2'],dataset['perturbationNumber'], dataset['parameterName'])
    #print(dataset['startStep'],dataset['endStep'])


#data = grbz[1]
#for i in data.keys():
#    print(i)
#    print(data[i])




'''
    
data = pd.DataFrame(grbz[1]['latLonValues'])
lats=data[0::3]
lons=data[1::3]
values=data[2::3]
print(len(lats),len(lons),len(values))
table = pd.DataFrame({'lats':lats,'lons':lons, 'values':values})


for filename in os.listdir('/home/ecmwf/'):
    if 'E' in filename:
        grbz = pygrib.open(filename)
        
'''