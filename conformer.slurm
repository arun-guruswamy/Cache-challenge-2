#!/bin/bash
#SBATCH -J conform_molecules
#SBATCH -c 1
#SBATCH --partition=dept_cpu
#SBATCH -o test_conform-%A_%a.out
#SBATCH -e test_conform-%A_%a.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu
#SBATCH --array=1-1

module load anaconda
source activate my-rdkit-env
cd $SLURM_SUBMIT_DIR

cmd=`sed -n "${SLURM_ARRAY_TASK_ID}p" conform_test_cmds.txt`

eval $cmd
exit