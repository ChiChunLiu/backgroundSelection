import msprime, pyslim, tskit, os, itertools
import numpy as np

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
        #print(ts.pairwise_diversity())

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


def theta_pi(sfs):
    n = len(sfs)
    num = (np.array(range(1, n + 1)) * np.array(range(n, 0, -1)) * sfs).sum()
    denum = n * (n + 1) / 2
    pi = num / denum
    return pi

def compute_diversity(ts_file):
    ts = pyslim.load(ts_file).simplify()
    return ts.pairwise_diversity()