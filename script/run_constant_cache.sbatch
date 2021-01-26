#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --partition=jnovembre
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --ntasks-per-node=14
#SBATCH --mem-per-cpu=2g
#SBATCH --account=pi-jnovembre
#SBATCH --job-name=dadi-cache
#SBATCH --output=nb-log-%J.out
#SBATCH --error=nb-log-%J.err

# activate the conda env 
source ~/.bashrc
conda activate bgs

python3 constant_N5000_cache.py -n $n
