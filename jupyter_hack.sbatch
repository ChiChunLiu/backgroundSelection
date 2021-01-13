#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --partition=jnovembre
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --ntasks-per-node=14
#SBATCH --mem-per-cpu=2g
#SBATCH --account=pi-jnovembre
#SBATCH --job-name=nb-tunnel
#SBATCH --output=nb-log-%J.out
#SBATCH --error=nb-log-%J.err

# activate the conda env 
source ~/.bashrc
conda activate bgs

ip=$(/sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}')
port=$((10000+ $RANDOM % 20000))
echo "http://"$ip":"$port"/"
jupyter lab --no-browser --ip=$ip --port=$port --log-level='ERROR'
