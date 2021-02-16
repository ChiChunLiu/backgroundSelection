import pickle, random, os
import numpy as np
import dadi
import argparse
import dadi.DFE as DFE
import matplotlib.pyplot as plt
from dadi.DFE import *
from scipy import stats
from dadi import *

def three_epoch(params, ns, pts):
    
    
    nuB,nuF,TB,TF,gamma = params

    xx = Numerics.default_grid(pts)
    phi = PhiManip.phi_1D(xx, gamma=gamma)

    phi = Integration.one_pop(phi, xx, TB, nuB, gamma = gamma)
    phi = Integration.one_pop(phi, xx, TF, nuF, gamma = gamma)

    fs = Spectrum.from_phi(phi, ns, (xx,))
    return fs
    
def constant_size(params, ns, pts):
    gamma = params[0]

    xx = Numerics.default_grid(pts)
    phi = PhiManip.phi_1D(xx, gamma=gamma)

    fs = Spectrum.from_phi(phi, ns, (xx,))
    return fs



my_parser = argparse.ArgumentParser()
my_parser.add_argument('-n','--nsample', action='store', type=int)
args = my_parser.parse_args()


demog_params = [0.1, 1, 0.5, 0.5]
theta_ns = 250.
ns = [args.nsample]

scale = 100
# Integrate over a range of gammas
pts_l = [960 * scale, 1280 * scale, 1600 * scale]

spectra = DFE.Cache1D(demog_params, ns, three_epoch, pts_l=pts_l, 
                      gamma_bounds=(1e-5, 300), gamma_pts=1000, verbose=True,
                      mp=True)
pickle.dump(spectra, open(f'../output/bottleneck_spectra_theta250_n{ns[0]}.bpkl','wb'))

