#!/bin/bash
#SBATCH -J RmWeight
#SBATCH -c 1
#SBATCH --partition=dept_cpu
#SBATCH -o RmWeight-%A_%a.out
#SBATCH -e RmWeight-%A_%a.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu
#SBATCH --array=1-5

module load anaconda
source activate sklearn-env
cd $SLURM_SUBMIT_DIR

cmd=`sed -n "${SLURM_ARRAY_TASK_ID}p" model_cmds.txt`

eval $cmd

exit

# 8046895 - Hyper-paramater Optimization 
# 8052272 - Sequential Random Search
