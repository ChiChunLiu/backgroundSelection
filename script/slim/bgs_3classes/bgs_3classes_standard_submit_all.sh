#!/bin/sh

for i in {1..100}; do
    for N in 5000; do
        sbatch --export=rep=$i,N=$N bgs_3classes_standard.sbatch && sleep 0.2
done; done
