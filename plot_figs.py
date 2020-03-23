import os
import sys
import matplotlib.pyplot as plt
from decimal import Decimal
import h5py
import numpy as np
from good_data import good_params

rootdir = os.path.dirname(os.path.realpath(__file__))
#print(rootdir)

data = []

for root, subdirs, files in os.walk(rootdir):
    if 'results.txt' in files:
        #print(root, subdirs, files)
        #print('------------------')
        
        with open(root + '/results.txt', 'r') as f:
            f.readline()
            Np = float(f.readline().rstrip())
            f.readline()
            Ra = float(f.readline().rstrip())
            f.readline()
            Ta = float(f.readline().rstrip())
            f.readline()
            Phi = float(f.readline().rstrip())
            f.readline()
            E_def = f.readline().rstrip()
        if E_def != 'nan':
            if [Phi, Np, Ta, Ra] in good_params:
                data.append([Phi, Np, Ta, Ra, float(E_def)])

#print(data)
colours = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
c_mark = 0

data.sort()

last_Np = data[0][1]
last_Ta = data[0][2]

Ra = []
E = []
legend = []
legend.append('Ta = %.2E' % Decimal(last_Ta))

'''fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xscale('log')'''

print('Plotting Np=%s graph:'%(last_Np))
for i in range(len(data)):
    #print(data[i])
    #print('--------------------')
    if data[i][1] == last_Np:
        if data[i][2] == last_Ta:
            Ra.append(data[i][3])
            E.append(data[i][4])
        else:
            plt.semilogx(Ra, E, color=colours[c_mark], marker='x', linestyle='None')
            c_mark += 1
            last_Ta = data[i][2]
            Ra = [data[i][3]]
            E = [data[i][4]]
            legend.append('Ta = %.2E' % Decimal(last_Ta))
    else:
        plt.xlabel('Ra')
        plt.ylabel('E')
        plt.xscale('log')
        plt.title('Np=%s'%(last_Np))
        plt.legend(legend)
        plt.savefig('%s/Np=%s.png' %(rootdir, last_Np))
        plt.clf()
        Ra = [data[i][3]]
        E = [data[i][4]]
        last_Ta = data[i][2]
        last_Np = data[i][1]
        legend = []
        legend.append('Ta = %.2E' % Decimal(last_Ta))
        print('Plotting Np=%s graph:'%(last_Np))

plt.xlabel('Ra')
plt.ylabel('E')
plt.xscale('log')
plt.legend(legend)
#print(legend)
plt.semilogx(Ra, E, color=colours[c_mark], marker='x', linestyle='None')
plt.title('Np=%s'%(last_Np))
plt.savefig('%s/Np=%s.png' %(rootdir, last_Np))




