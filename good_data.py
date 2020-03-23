import os
import h5py
import numpy as np

rootdir = ['/home/da330/Dedalus/results_raw/', '/home/db463/Dedalus/2020/results_raw/', '/home/nbh202/dedalus/all/results_raw/', '/home/nbh202/dedalus/all/sim2/results_raw/']
#rootdir = ['C:\\Users\\Domas\\Desktop\\Dedalus_figs\\results_png_txt_da330\\Np=0.50\\Ra=5.00E+05\\Ta=1.00E+06\\Phi=45\\']

good_params = []

for rd in rootdir:
    for root, subdirs, files in os.walk(rd):
        if 'raw_data' in subdirs:
            good_data = False
            for root2, subdirs2, files2 in os.walk(root + '/raw_data/analysis/'):
                for f in files2:
                    if '.h5' in f:
                        with h5py.File(root2 + "/" + f, mode='r') as file:
                            ana_t = np.array(file['scales']['sim_time'])
                            if float(ana_t[-1]) > 3: good_data = True
            if good_data:
                for root2, subdirs2, files2 in os.walk(root + '/raw_data/run_parameters/'):
                    for f in files2:
                        if '.h5' in f:
                            with h5py.File(root2 + "/" + f, mode='r') as file:
                                Ra = file['tasks']['Ra'][0][0][0]
                                Np = float(file['tasks']['Np'][0][0][0])
                                Ta = file['tasks']['Ta'][0][0][0]
                                Phi = int(file['tasks']['Phi'][0][0][0])
                                good_params.append([Phi, Np, Ta, Ra])

#print(len(good_params))
