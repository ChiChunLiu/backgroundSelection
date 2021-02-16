#!/bin/sh
# properties = {"type": "single", "rule": "simulate_BGS_focal", "local": false, "input": ["/project2/jnovembre/ccliu/backgroundSelection/scripts/slim/bgs_focal.slim"], "output": ["/project2/jnovembre/ccliu/backgroundSelection/data/slim/bgs_1class/bgs_focal.rep16.trees"], "wildcards": {"rep": "16"}, "params": {}, "log": [], "threads": 1, "resources": {"cpus": 1, "mem_mb": 500, "time_min": 180, "partition": "jnovembre"}, "jobid": 316, "cluster": {}}
 cd /project2/jnovembre/ccliu/backgroundSelection && \
PATH='/scratch/midway2/chichun/miniconda3/envs/bgs/bin':$PATH /scratch/midway2/chichun/miniconda3/envs/bgs/bin/python3.8 \
-m snakemake /project2/jnovembre/ccliu/backgroundSelection/data/slim/bgs_1class/bgs_focal.rep16.trees --snakefile /project2/jnovembre/ccliu/backgroundSelection/workflow/snakefile.py \
--force -j --keep-target-files --keep-remote --max-inventory-time 0 \
--wait-for-files /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.5mhz0o8z /project2/jnovembre/ccliu/backgroundSelection/scripts/slim/bgs_focal.slim /project2/jnovembre/ccliu/backgroundSelection/.snakemake/conda/07ca9279 --latency-wait 5 \
 --attempt 1 --force-use-threads --scheduler ilp \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules simulate_BGS_focal --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-conda  --default-resources "cpus=1" "mem_mb=2000" "time_min=60" "partition=\"jnovembre\""  && touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.5mhz0o8z/316.jobfinished || (touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.5mhz0o8z/316.jobfailed; exit 1)

