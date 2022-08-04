#!/bin/bash
#SBATCH -J select_molecules
#SBATCH -c 1
#SBATCH --partition=dept_cpu
#SBATCH -o select-%A.out
#SBATCH -e select-%A.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu

python3 select_molecules.py

exit