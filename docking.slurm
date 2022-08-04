#!/bin/bash
#SBATCH -J docking
#SBATCH -c 4
#SBATCH --mem=12GB
#SBATCH --partition=dept_gpu
#SBATCH -o docking_output/docked-%A_%a.out
#SBATCH -e docking_output/docked-%A_%a.err
#SBATCH --mail-type=fail
#SBATCH --mail-user=aguruswamy@vassar.edu
#SBATCH --array=1-500%100
#SBATCH --gres=gpu:1
#SBATCH --exclude=g102,g104,g122,g123

export PATH=/net/pulsar/home/koes/dkoes/local/bin:$PATH
export LD_LIBRARY_PATH=/net/pulsar/home/koes/dkoes/local/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/net/pulsar/home/koes/dkoes/git/rdkit/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/net/pulsar/home/koes/dkoes/local/lib/python3.8/site-packages/:/net/pulsar/home/koes/dkoes/git/rdkit:/net/pulsar/home/koes/dkoes/git/rdkit/Contrib:$PYTHONPATH

#module load cuda
cd $SLURM_SUBMIT_DIR

cmd=`sed -n "${SLURM_ARRAY_TASK_ID}p" docking_cmds.txt`

eval $cmd
exit