#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --partition=jnovembre
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=500m
#SBATCH --account=pi-jnovembre
#SBATCH --job-name=nb-tunnel
#SBATCH --output=nb-log-%J.out
#SBATCH --error=nb-log-%J.err

# activate the conda env 
source ~/.bashrc
conda activate bgs


gamma=$(python3 infer_mle_gamma.py -f "$file" -n "$n" -c "$c")

echo "$file $n $c $gamma" >> $out
