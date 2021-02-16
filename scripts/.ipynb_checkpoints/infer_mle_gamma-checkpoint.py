#!/usr/bin/env python
# coding: utf-8
import msprime, pyslim, tskit
from scipy.integrate import quad
from scipy.stats import binom
from scipy.optimize import minimize_scalar
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, help="file path")
parser.add_argument("-c", "--cutoff", type=int, help="cutoff for SFS")
parser.add_argument("-n", "--nsample", type=int, help="sample size")
args = parser.parse_args()


def f(q, gamma):
    return 1 / (q * (1 - q)) * (1 - np.exp(-2 * gamma * (1 - q))) / (1 - np.exp(-2 * gamma))

def F_integrand(q, gamma, i, n):
    return f(q, gamma) * binom.pmf(i, n, q)

def F(gamma, i, n):
    return quad(F_integrand, 1e-5, 1-1e-5, args=(gamma, i, n))[0]


def SFS(gamma, theta, n = 200):
    sfs = []
    for i in range(1, n):
        mu = F(gamma, i, n)
        sfs.append(theta * mu)
    return np.array(sfs)


def profile_likelihood(gamma, sfs, cutoff):
    n = len(sfs) + 1
    S = sfs.sum() # num. segregated sites
    
    F_tot = 0
    for i in range(1 + cutoff, n - cutoff):
        F_tot += F(gamma, i, n)
    theta_hat = S / F_tot
    
    loglik = 0
    for i in range(1 + cutoff, n - cutoff):
        loglik += sfs[i-1] * np.log(theta_hat * F(gamma, i, n))
    loglik -= theta_hat * F_tot
    
    return -loglik

def gamma_mle(sfs, m, M, cutoff):
    res = minimize_scalar(lambda g: profile_likelihood(g, sfs=sfs, cutoff=cutoff),
                          bounds=(m, M), 
                          method='bounded')
    return res.x

def compute_gamma_mle(afs, cutoff=0):
    gamma = gamma_mle(afs[:,2], m=-500, M=-1, cutoff=cutoff)
    return gamma


def allele_counts(ts, sample_sets=None):
    if sample_sets is None:
        sample_sets = [ts.samples()]
    def f(x):
        return x
    return ts.sample_count_stat(sample_sets, f, len(sample_sets),
               span_normalise=False, windows='sites',
               polarised=True, mode='site', strict=False)


def get_afss(ts_file, sample_size = None):
    if sample_size:
        ts = pyslim.load(ts_file).simplify()
        keep_indivs = np.random.choice(ts.individuals_alive_at(0), 
                                       sample_size, replace=False)
        keep_nodes = []
        for i in keep_indivs:
            keep_nodes.extend(ts.individual(i).nodes)
        ts = ts.simplify(keep_nodes)

    mut_type = np.zeros(ts.num_sites)
    for j, s in enumerate(ts.sites()):
        mt = []
        for m in s.mutations:
            for md in m.metadata:
                mt.append(md.mutation_type)
        if len(set(mt)) > 1:
            mut_type[j] = 4
        else:
            mut_type[j] = mt[0]

    freqs = allele_counts(ts)
    l = len(ts.samples())
    freqs = freqs.flatten().astype(int)
    mut_afs = np.zeros((l + 1, 4), dtype='int64')
    for k in range(4):
        mut_afs[:, k] = np.bincount(freqs[mut_type == k+1], 
                                    minlength=l + 1)
    
    return mut_afs[1:(2 * sample_size),:]


afs = get_afss(args.file, sample_size = args.nsample)
print(f'{compute_gamma_mle(afs, args.cutoff):.3f}')
