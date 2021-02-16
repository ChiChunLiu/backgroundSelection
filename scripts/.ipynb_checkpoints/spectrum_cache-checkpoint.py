import pickle, random, os, dadi
import dadi.DFE as DFE
from dadi.DFE import *
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

ns = [snakemake.wildcards.ns]
mode = snakemake.wildcards.cache_demo


scale = 100
# Integrate over a range of gammas
pts_l = [960 * scale, 1280 * scale, 1600 * scale]

if mode == 'constant':
    spectra = DFE.Cache1D([], ns, constant_size, pts_l=pts_l,
                          gamma_bounds=(1e-5, 300), gamma_pts=1000, verbose=True,
                          mp=True)
    pickle.dump(spectra, open(f'output/constant_spectra_n{ns[0]}.bpkl','wb'))

elif mode == 'bottleneck':
    demog_params = [0.1, 1, 0.5, 0.5]
    spectra = DFE.Cache1D(demog_params, ns, three_epoch, pts_l=pts_l, 
                          gamma_bounds=(1e-5, 300), gamma_pts=1000, verbose=True,
                          mp=True)
    pickle.dump(spectra, open(f'output/bottleneck_spectra_n{ns[0]}.bpkl','wb'))

else:
    pass
