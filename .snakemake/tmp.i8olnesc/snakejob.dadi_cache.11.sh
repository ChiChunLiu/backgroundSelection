#!/bin/sh
# properties = {"type": "single", "rule": "dadi_cache", "local": false, "input": ["/project2/jnovembre/ccliu/backgroundSelection/scripts/test.py"], "output": ["/project2/jnovembre/ccliu/backgroundSelection/output/constant_spectra_n35.bpkl"], "wildcards": {"cache_demo": "constant", "ns": "35"}, "params": {}, "log": [], "threads": 1, "resources": {"cpus": 1, "mem_mb": 2000, "time_min": 60, "partition": "jnovembre"}, "jobid": 11, "cluster": {}}
 cd /project2/jnovembre/ccliu/backgroundSelection && \
PATH='/scratch/midway2/chichun/miniconda3/envs/bgs/bin':$PATH /scratch/midway2/chichun/miniconda3/envs/bgs/bin/python3.8 \
-m snakemake /project2/jnovembre/ccliu/backgroundSelection/output/constant_spectra_n35.bpkl --snakefile /project2/jnovembre/ccliu/backgroundSelection/workflow/snakefile.py \
--force -j --keep-target-files --keep-remote --max-inventory-time 0 \
--wait-for-files /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.i8olnesc /project2/jnovembre/ccliu/backgroundSelection/scripts/test.py --latency-wait 5 \
 --attempt 1 --force-use-threads --scheduler ilp \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules dadi_cache --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-conda  --default-resources "cpus=1" "mem_mb=2000" "time_min=60" "partition=\"jnovembre\""  && touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.i8olnesc/11.jobfinished || (touch /project2/jnovembre/ccliu/backgroundSelection/.snakemake/tmp.i8olnesc/11.jobfailed; exit 1)

