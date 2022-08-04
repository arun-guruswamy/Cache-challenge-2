#!/bin/bash
#SBATCH -J minimize_queries
#SBATCH -c 1
#SBATCH --partition=dept_gpu
#SBATCH -o 2ndIter-%A_%a.out
#SBATCH -e 2ndIter-%A_%a.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu
#SBATCH --array=1-3
#SBATCH --mem=1GB

export PATH=/net/pulsar/home/koes/dkoes/local/bin:$PATH
export LD_LIBRARY_PATH=/net/pulsar/home/koes/dkoes/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/net/pulsar/home/koes/dkoes/git/rdkit/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/net/pulsar/home/koes/dkoes/local/lib/python3.8/site-packages/:/net/pulsar/home/koes/dkoes/git/rdkit:/net/pulsar/home/koes/dkoes/git/rdkit/Contrib:$PYTHONPATH

module load cuda
cd $SLURM_SUBMIT_DIR

cmd=`sed -n "${SLURM_ARRAY_TASK_ID}p" minimize_errr_queries.txt`

eval $cmd
exit

