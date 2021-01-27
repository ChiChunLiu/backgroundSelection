#!/bin/bash
#SBATCH --time=10:00:00
#SBATCH --partition=jnovembre
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2g
#SBATCH --job-name=slim_neutral
#SBATCH --output=slim-%J.out
#SBATCH --error=slim-%J.err

# activate the conda env 
source ~/.bashrc
conda activate bgs

start=`date +%s`
slim -d rep=$rep -d N=$N -m ./bgs_3classes_bottleneck.3classes.slim
end=`date +%s`

runtime=$((end-start))

echo $runtime
