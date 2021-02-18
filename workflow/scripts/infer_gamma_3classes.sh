#!/bin/sh

while IFS=" " read -r file n c out
do
   #echo "$file $n $c $out"
   sbatch --export=file=$file,n=$n,c=$c,out=$out infer_gamma_3classes.sbatch && sleep 0.2
done < "file_list.txt"
