#!/bin/bash -l
 
#SBATCH --job-name=python_pretrain_ESD
#SBATCH --output=job-%j.output
#SBATCH --error=job-%j.error
#SBATCH --time=50:00:00
#SBATCH --mem=102400
## GPU requirements
#SBATCH --gres gpu:1
## Specify partition
#SBATCH -p gpu
 
# Change directory to the temporary directory on the compute node
cd /mnt/scratch/users/dc2020/SOTS/
 
flight start
 
# Activate Gridware
flight env activate conda@gpu

export PYTHONPATH=/mnt/scratch/users/dc2020/SOTS/lib

python tracking/train_sot.py --cfg experiments/SiamDW.yaml

python tracking/test_sot.py --cfg experiments/SiamDW.yaml --resume snapshot/checkpoint_e20.pth --dataset OTB2015

python tracking/eval_sot.py --dataset OTB2015 --trackers SiamDWcheckpoint_e20
