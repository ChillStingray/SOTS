#!/bin/bash
echo ""
echo ""
echo "****************** Installing matplotlib 2.2.2 ******************"
conda install -y matplotlib=3.2.2

echo ""
echo ""
echo "****************** Installing pandas ******************"
conda install -y pandas

echo ""
echo ""
echo "****************** Installing opencv ******************"
pip install opencv-python

echo ""
echo ""
echo "****************** Installing tensorboardX ******************"
pip install tensorboardX

echo ""
echo ""
echo "****************** Installing cython ******************"
conda install -y cython


echo ""
echo ""
echo "****************** Installing skimage ******************"
pip install scikit-image



echo ""
echo ""
echo "****************** Installing pillow ******************"
pip install 'pillow<7.0.0'

echo ""
echo ""
echo "****************** Installing scipy ******************"
pip install scipy

echo ""
echo ""
echo "****************** Installing shapely ******************"
pip install shapely

echo ""
echo ""
echo "****************** Installing easydict ******************"
pip install easydict

echo ""
echo ""
echo "****************** Installing jpeg4py python wrapper ******************"
pip install jpeg4py 
pip install mpi4py
pip install ray==0.8.7
pip install hyperopt


echo ""
echo ""
echo "****************** Installing wandb ******************"
pip install wandb


echo ""
echo ""
echo "****************** Installing vot python toolkit ******************"
# pip install git+https://github.com/votchallenge/vot-toolkit-python@92241358a172e6815c8b5c4a24a1e89b6d2864a9

echo "****************** Installation complete! ******************"
