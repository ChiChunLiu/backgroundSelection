import numpy as np
configfile: 'config/config.yaml'

    
N = 5000
N_bottleneck = 500

Bs = [0.4, 0.6, 0.8] # strengths of BGS
ss = [2e-4, 2e-3, 2e-2, 2e-1] # selection coeffs of focal sites
Ns = [2000, 3000, 4000, 5000] # population sizes
reps = np.arange(1, 101, dtype=int) # n. of replicates
cache_spectrum_nss = np.arange(10, 15, 5, dtype=int) # sfs sample sizes
demo_models = ['constant', 'bottleneck']
rs = [0, 0.1, 0.2] # recombination rates

rule run_all:
    input:
        expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_1class.B{B}_N5000_rep{rep}.trees'), rep = reps, B = Bs),
        expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_focal.rep{rep}.trees'), rep = reps),
        expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes/bgs_3classes.B{B}_N{N}_rep{rep}.trees'), B = Bs, rep = reps, N = Ns),
        expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep{rep}.trees'), rep = reps),
        expand('{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500_rep{rep}.trees'), rep = reps),
        expand('{}/{}'.format(config['paths']['output'], '{cache_demo}_spectra_n{ns}.bpkl'), ns = cache_spectrum_nss, cache_demo = demo_models)


rule simulate_BGS_validation:
    '''
    simulate simplest scenarios for BGS strength validation. 
    Associated with the notebook BGS_validation
    '''
    params:
        sim_script = '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_1class.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_1class.B{B}_N5000_rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N={wildcards.N} -d B={wildcards.B} -m {params.sim_script}"

rule simulate_BGS_focal:
    '''
    simulate BGS generated from focal sites
    '''
    params:
        sim_script = '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_focal.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_1class/bgs_focal.rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N={wildcards.N} -m {params.sim_script}"

rule simulate_constant_size:
    '''
    simulate constant sized populations from bgs_3classes_standard.slim
    '''
    params:
        sim_script = '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_standard.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes/bgs_3classes.B{B}_N{N}_rep{rep}.trees')
    resources: mem_mb=500, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        "slim -d rep={wildcards.rep} -d N={wildcards.N} -d B={wildcards.B} -m {params.sim_script}"


rule simulate_bottleneck_no_mutation:
    '''
    simulate from bgs_3classes_bottleneck.slim with no mutation
    '''
    params:
        sim_script = '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep{rep}.trees')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        """slim -d u=0 -d rep={wildcards.rep} -d N=500 -d "mode='noMutation'" -m {params.sim_script}"""
    

rule simulate_bottleneck:
    '''
    simulate from bgs_3classes_bottleneck.slim  
    '''
    params:
        sim_script = '{}/{}'.format(config['paths']['scripts'], 'slim/bgs_3classes_bottleneck.slim')
    output:
        '{}/{}'.format(config['paths']['data'], 'slim/bgs_3classes_noneq/bgs_bottleneck_3classes.N500_rep{rep}.trees')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        """slim -d u=1e-7 -d rep={wildcards.rep} -d N={wildcards.N_bottleneck} -d "mode='3classes'" -m {params.sim_script}"""

        
rule simulate_prf_bottleneck:
    '''
    simulate from PReFerSim
    '''
    params:
        par = '{}/{}'.format(config['paths']['params'], 'PReFerSim/bottleneck/param.txt')
        demog = '{}/{}'.format(config['paths']['params'], 'PReFerSim/bottleneck/demog.txt')
    output:
        full = '{}/{}'.format(config['paths']['data'], 'PReFerSim/bottleneck/Output.{rep}.full_out.txt')
        popsfs = '{}/{}'.format(config['paths']['data'], 'PReFerSim/bottleneck/Output.{rep}.popsfs_out.txt')
        sfs = '{}/{}'.format(config['paths']['data'], 'PReFerSim/bottleneck/Output.{rep}.sfs_out.txt')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        """GSL_RNG_SEED={wildcards.rep} GSL_RNG_TYPE=mrg utils/PReFerSim {params.par} {wildcards.rep}"""
        
        
rule simulate_prf_constant_size:
    '''
    simulate from PReFerSim
    '''
    params:
        par = '{}/{}'.format(config['paths']['params'], 'PReFerSim/constant/param.txt')
        demog = '{}/{}'.format(config['paths']['params'], 'PReFerSim/constant/demog.txt')
    output:
        full = '{}/{}'.format(config['paths']['data'], 'PReFerSim/constant/Output.{rep}.full_out.txt')
        popsfs = '{}/{}'.format(config['paths']['data'], 'PReFerSim/constant/Output.{rep}.popsfs_out.txt')
        sfs = '{}/{}'.format(config['paths']['data'], 'PReFerSim/constant/Output.{rep}.sfs_out.txt')
    resources: mem_mb=200, time_min=180
    conda: 'envs/slim.yaml'
    shell:
        """GSL_RNG_SEED={wildcards.rep} GSL_RNG_TYPE=mrg utils/PReFerSim {params.par} {wildcards.rep}"""
   
rule dadi_cache:
    '''
    create cache spectrum files 
    '''
    output:
        '{}/{}'.format(config['paths']['output'], '{cache_demo}_spectra_n{ns}.bpkl')
    resources: ntasks_per_node=14, mem_mb=2000, nodes=1
    conda: 'envs/dadi.yaml'
    script:
        '{}/{}'.format(config['paths']['scripts'], 'spectrum_cache.py')
