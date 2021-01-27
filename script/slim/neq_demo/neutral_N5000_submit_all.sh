#!/bin/sh

for i in {1..10}; do
    sbatch --export=rep=$i neutral_N5000.sbatch && sleep 0.2
done
