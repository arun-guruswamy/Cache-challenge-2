#!/bin/bash
#SBATCH -J generate_fingerprints
#SBATCH -c 1
#SBATCH --partition=dept_cpu
#SBATCH -o fingerprints-%A.out
#SBATCH -e fingerprints-%A.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu

module load anaconda
source activate sklearn-env
cd $SLURM_SUBMIT_DIR

python3 generate_fingerprints.py

exit