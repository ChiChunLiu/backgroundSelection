#!/bin/sh
#SBATCH --time=24:00:00
#SBATCH --partition=jnovembre
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=500m
#SBATCH --account=pi-jnovembre
#SBATCH --job-name=nb-tunnel
#SBATCH --output=nb-log-%J.out
#SBATCH --error=nb-log-%J.err



module load gsl


GSL_RNG_SEED=$i GSL_RNG_TYPE=mrg ../../../../PReFerSim/PReFerSim bottleneck_param.txt $i




