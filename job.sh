#!/bin/bash -l
 
#SBATCH --job-name=python_pretrain_ESD
#SBATCH --output=job-%j.output
#SBATCH --error=job-%j.error
#SBATCH --time=24:00:00
#SBATCH --mem=102400
## GPU requirements
#SBATCH --gres gpu:1
## Specify partition
#SBATCH -p gpu
 
# Change directory to the temporary directory on the compute node
cd /mnt/scratch/users/dc2020/SOTS
 
flight start
 
# Activate Gridware
flight env activate conda@SOTS
 
python tracking/train_sot.py --cfg experiments/SiamDW.yaml
