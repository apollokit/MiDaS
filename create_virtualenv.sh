#!/bin/bash
set -ex

SCRIPT_DIR=$(dirname $(realpath $0))
# python_version=3.7.9
python_version=3.7

conda create -n midas python=$python_version anaconda
# for the below: https://github.com/conda/conda/issues/7980
source ~/anaconda3/etc/profile.d/conda.sh
conda activate midas
# pip3 install -r requirements.txt
conda install pytorch==1.7.0 torchvision opencv -c pytorch