
def create_param_file(mutation_rate = 250,
                     dfetype = 'point', 
                     printsfs = 1, 
                     printsiteinfo = 1, 
                     n = 1000, 
                     selcoeff = 0.01, 
                     demo_hist, 
                     dfe_info, 
                     outfile):
    '''
    note this only works for point dfe
    '''
    assert dfetype == 'point'
    
    with open(outfile) as f:
        f.write(f'MutationRate: {mutation_rate}\n')
        f.write(f'DemographicHistory: {demo_hist}\n')
        f.write(f'DFEType: {dfetype}\n')
        f.write(f'DFEPointSelectionCoefficient: {selcoeff}\n')
        f.write(f'PrintSFS: {printsfs}\n')
        f.write(f'PrintSegSiteInfo: {printsiteinfo}\n')
        f.write(f'n: {n}\n')

def create_demog_file(demog, outfile):
    if demog == 'bottleneck':
        with open(outfile) as f:
            f.write(f'10000 100000\n')
            f.write(f'1000 5000\n')
            f.write(f'10000 5000\n')
    elif demog == 'constant':
        with open(outfile) as f:
            f.write(f'10000 100000\n')
    

create_param_file(snakemake.output.param)
create_demog_file(snakemake.output.demog)