#!/bin/bash

#SBATCH --job-name=jn

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=dept_cpu
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=None
#SBATCH --mem=12GB
#SBATCH --error=jupyter_cpu.stderr
#SBATCH --output=jupyter_cpu.stdout
## get tunneling info
XDG_RUNTIME_DIR=""
ipnport=$(shuf -i8000-9999 -n1)
ipnip=$(hostname -i)
## print tunneling instructions to jupyter-log-{jobid}.txt
echo -e "
Copy/Paste this in your local terminal to ssh tunnel with remote
-----------------------------------------------------------------
ssh -N -L $ipnport:$ipnip:$ipnport USER@cluster.csb.pitt.edu
-----------------------------------------------------------------
Then open a browser on your local machine to the following address
------------------------------------------------------------------
localhost:$ipnport  (prefix w/ https:// if using password)
------------------------------------------------------------------
"
## start an ipcluster instance and launch jupyter server
source ~/.bashrc
module load anaconda
source activate sklearn-env
export LD_LIBRARY_PATH=""
export PYTHONPATH=""
jupyter lab --NotebookApp.iopub_data_rate_limit=100000000000000 \
   --port=$ipnport --ip=$ipnip --NotebookApp.password='' --NotebookApp.token='' --no-browser