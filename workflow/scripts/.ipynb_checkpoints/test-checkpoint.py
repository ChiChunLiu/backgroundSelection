
with open(snakemake.output[0], 'w') as f:
    f.write(snakemake.wildcards.ns)
    f.write(snakemake.wildcards.cache_demo)
    
