#!/bin/sh
# properties = {"type": "single", "rule": "simulate_bottleneck_no_mutation", "local": false, "input": ["/project2/jnovembre/ccliu/backgroundSelection/scripts/slim/bgs_3classes_bottleneck.slim"], "output": ["/project2/jnovembre/ccliu/backgroundSelection/data/slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep5.trees"], "wildcards": {"rep": "5"}, "params": {}, "log": [], "threads": 1, "resources": {"cpus": 1, "mem_mb": 200, "time_min": 180, "partition": "jnovembre"}, "jobid": 525, "cluster": {}}
 cd /project2/jnovembre/ccliu/backgroundSelection && \
PATH='/scratch/midway2/chichun/miniconda3/envs/bgs/bin':$PATH /scratch/midway2/chichun/miniconda3/envs/bgs/bin/python3.8 \
-m snakemake /project2/jnovembre/ccliu/backgroundSelection/data/slim/bgs_3classes_noneq/bgs_bottleneck_noMutation.N500_rep5.trees --snakefile /project2/jnovembre/ccliu/backgroundSelection/workflow/snakefile.py \
--force -j --keep-target-files --keep-remote --max-inventory-time 0 \
--wait-for-files /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.g6vqmcz_ /project2/jnovembre/ccliu/backgroundSelection/scripts/slim/bgs_3classes_bottleneck.slim --latency-wait 5 \
 --attempt 1 --force-use-threads --scheduler ilp \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules simulate_bottleneck_no_mutation --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-conda  --default-resources "cpus=1" "mem_mb=2000" "time_min=60" "partition=\"jnovembre\""  && touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.g6vqmcz_/525.jobfinished || (touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.g6vqmcz_/525.jobfailed; exit 1)

