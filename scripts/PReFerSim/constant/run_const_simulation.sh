#!/bin/zsh


for i in {1..5}; do
    GSL_RNG_SEED=$i GSL_RNG_TYPE=mrg ../../../PReFerSim/PReFerSim const_param.txt $i
done

