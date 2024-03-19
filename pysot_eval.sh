#!/bin/bash -l

#BATCH --job-name=python_pretrain_ESD
#SBATCH --output=job-%j.output
#SBATCH --error=job-%j.error
#SBATCH --time=24:00:00
#SBATCH --mem=102400
## GPU requirements
#SBATCH --gres gpu:1
## Specify partition
#SBATCH -p gpu

# Change directory to the temporary directory on the compute node
cd /mnt/scratch/users/dc2020/SOTS/lib/evaluator/vot_eval

flight start

# Activate Gridware
flight env activate conda@gpu

python bin/eval.py --dataset_dir ../../../dataset/OTB2015 --dataset OTB --tracker_result_dir ../../../result/OTB2015/SiamDW --trackers SiamDW --num 1 --show_video_level --vis
