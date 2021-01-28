#!/bin/sh

for i in {1..100}; do
    for N in 500; do
    sbatch --export=rep=$i,N=$N bgs_3classes_bottleneck.3classes.sbatch  && sleep 0.2
done; done
