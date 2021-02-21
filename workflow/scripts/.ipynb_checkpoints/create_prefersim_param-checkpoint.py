
def create_param_file(demo_hist, 
                      outfile,
                      prefix,
                      mutation_rate = 250,
                      dfetype = 'point', 
                      printsfs = 1, 
                      printsiteinfo = 1, 
                      ns = 1000, 
                      selcoeff = 0.01, 
                     ):
    '''
    note this only works for point dfe
    '''
    assert dfetype == 'point'
    
    with open(outfile, 'w') as f:
        f.write(f'MutationRate: {mutation_rate}\n')
        f.write(f'DemographicHistory: {demo_hist}\n')
        f.write(f'DFEType: {dfetype}\n')
        f.write(f'DFEPointSelectionCoefficient: {selcoeff}\n')
        f.write(f'PrintSFS: {printsfs}\n')
        f.write(f'PrintSegSiteInfo: {printsiteinfo}\n')
        f.write(f'n: {ns}\n')
        f.write(f'FilePrefix: {prefix}')

def create_demog_file(demog, outfile):
    if demog == 'bottleneck':
        with open(outfile, 'w') as f:
            f.write(f'10000 100000\n')
            f.write(f'1000 5000\n')
            f.write(f'10000 5000\n')
    elif demog == 'constant':
        with open(outfile, 'w') as f:
            f.write(f'10000 100000\n')


if snakemake.rule == 'create_PReFerSim_demogs':
    create_demog_file(demog = snakemake.wildcards.demo_model,
                      outfile = snakemake.output.demog)
elif snakemake.rule == 'create_PReFerSim_params':
    file_prefix = f'{snakemake.wildcards.demo_model}_n{snakemake.wildcards.ns}_rep' 
    create_param_file(demo_hist = snakemake.params.demog, 
                      ns = snakemake.wildcards.ns, 
                      outfile = snakemake.output.param, 
                      prefix = '{}/{}'.format(snakemake.params.out_dir, file_prefix))
