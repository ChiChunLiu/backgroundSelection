import numpy as np
configfile: 'config/config.yaml'

N = 5000
mu = 6.25 * 1e-7
l = 5e5
Ud = mu * l * 4/25
Bs = [0.4, 0.8]
ss_bgs = [2 * Ud / np.log(B) for B in Bs] # selection coeffs for bgs
ss = [2e-4, 2e-3, 2e-2, 2e-1] # selection coeffs of focal sites
Ns = [4000, 5000] # population sizes
reps = list(range(1, 3)) # n. of replicates
cache_spectrum_nss = list(range(10, 51, 5)) # sfs sample sizes
demo_models = ['constant', 'bottleneck']
rs = [0, 0.1, 0.2] # recombination rates

## start of the rules
rule run_all:
    input:
        expand('{}/{}'.format(config['paths']['data'], 'bgs_1class/bgs_1class.B{B}_N{N}_rep{rep}.trees'), rep = reps, B = Bs, N = Ns)
        #expand('{}/{}'.format(config['path']['data'], 'bgs_3classes/bgs_3classes_N{N}_rep{rep}.trees'), rep = reps, N = Ns),
        #expand('{}/{}'.format(config['path']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500rep{rep}.trees'), rep = reps),
        #expand('{}/{}'.format(config['path']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500rep{rep}.trees'), rep = reps),
        #expand('{}/{}'.format(config['path']['output'], '{cache_demo}_spectra_n{ns}.bpkl'), ns = cache_spectrum_nss, cache_demo = demo_models)


rule simulate_BGS_validation:
    '''
    simulate simplest scenarios for BGS strength validation
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_1class.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'bgs_1class/bgs_1class.B{B}_N{N}_rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N={wildcards.N} -d B={wildcards.B} -m {input}"



rule simulate_constant_size_vary_N:
    '''
    simulate constant sized populations from bgs_3classes_standard.slim
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_standard.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'bgs_3classes/bgs_3classes_N{N}_rep{rep}.trees')
    run:
        shell("slim -d rep={rep} -d N={N} -m {input}")


rule simulate_bottleneck:
    '''
    simulate from bgs_3classes_bottleneck.slim  
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500rep{rep}.trees')
    run:
        shell("slim -d u={base_mutation_rate} -d rep={rep} -d N=500 -m {input}")

rule simulate_bottleneck_no_mutation:
    '''
    simulate from bgs_3classes_bottleneck.slim with no mutation
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500rep{rep}.trees')
    run:
        shell("slim -d u=0 -d rep={rep} -d N=500 -m {input}")


rule dadi_cache:
    '''
    create cache spectrum files 
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'spectrum_cache.py')
    output:
        '{}/{}'.format(config['paths']['output'], '{cache_demo}_spectra_n{ns}.bpkl')
    run:
        shell("python3 {input} -m {cache_demo} -n {ns}")

#rule simulate_contraction:
#    '''
#    simulate from bgs_3classes_contraction.slim
#    '''
#    pass