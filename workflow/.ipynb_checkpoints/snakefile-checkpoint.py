import numpy as np
configfile: 'config/config.yaml'

N = 5000
mu = 6.25 * 1e-7
l = 5e5
Ud = mu * l * 4/25
Bs = [0.4, 0.6, 0.8]
ss_bgs = [2 * Ud / np.log(B) for B in Bs] # selection coeffs for bgs
ss = [2e-4, 2e-3, 2e-2, 2e-1] # selection coeffs of focal sites
Ns = [2000, 3000, 4000, 5000] # population sizes
reps = list(range(1, 11)) # n. of replicates
cache_spectrum_nss = list(range(10, 15, 5)) # sfs sample sizes
demo_models = ['constant', 'bottleneck']
rs = [0, 0.1, 0.2] # recombination rates

## start of the rules
rule run_all:
    input:
#         expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_1class.B{B}_N5000_rep{rep}.trees'), rep = list(range(1,101)), B = Bs),
#         expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_focal.rep{rep}.trees'), rep = list(range(1,101))),
#         expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes/bgs_3classes.B{B}_N{N}_rep{rep}.trees'), B = Bs, rep = reps, N = Ns),
#         expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep{rep}.trees'), rep = list(range(1,11))),
#         expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500_rep{rep}.trees'), rep = list(range(1,11))),
        expand('{}/{}'.format(config['paths']['output'], '{cache_demo}_spectra_n{ns}.bpkl'), ns = cache_spectrum_nss, cache_demo = demo_models)


rule simulate_BGS_validation:
    '''
    simulate simplest scenarios for BGS strength validation. 
    Associated with the notebook BGS_validation
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_1class.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_1class.B{B}_N5000_rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N=5000 -d B={wildcards.B} -m {input}"

rule simulate_BGS_focal:
    '''
    simulate BGS generated from focal sites
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_focal.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_focal.rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N=5000 -m {input}"

rule simulate_constant_size:
    '''
    simulate constant sized populations from bgs_3classes_standard.slim
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_standard.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes/bgs_3classes.B{B}_N{N}_rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N={wildcards.N} -d B={wildcards.B} -m {input}"


rule simulate_bottleneck_no_mutation:
    '''
    simulate from bgs_3classes_bottleneck.slim with no mutation
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep{rep}.trees')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    run:
        shell("""slim -d u=0 -d rep={wildcards.rep} -d N=500 -d "mode='noMutation'" -m {input}""")
        

rule simulate_bottleneck:
    '''
    simulate from bgs_3classes_bottleneck.slim  
    '''
    input:
        '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500_rep{rep}.trees')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    run:
        shell("""slim -d u=1e-7 -d rep={wildcards.rep} -d N=500 -d "mode='3classes'" -m {input}""")
        


rule dadi_cache:
    '''
    create cache spectrum files 
    '''
    output:
        '{}/{}'.format(config['paths']['output'], '{cache_demo}_spectra_n{ns}.bpkl')
    resources: mem_mb=200, time_min=420
    conda: 'envs/dadi.yaml'
    script:
        '{}/{}'.format(config['paths']['scripts'], 'spectrum_cache.py')