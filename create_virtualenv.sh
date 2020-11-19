#!/bin/bash
set -ex

SCRIPT_DIR=$(dirname $(realpath $0))
# python_version=3.7.9
python_version=3.7

# conda create -n midas python=$python_version anaconda
# for the below: https://github.com/conda/conda/issues/7980
# source ~/anaconda3/etc/profile.d/conda.sh
# conda activate midas
# pip3 install -r requirements.txt
# conda install pytorch==1.7.0 torchvision opencv -c pytorch

virtualenv_dir=~/.config/vinci/virtualenvs/midas

# If the virtualenv already exists, just update requirements.
if [ -e "$virtualenv_dir" ]; then
    echo "$virtualenv_dir already exists. We'll just update requirements."
else
    /usr/bin/python${python_version} -m venv "$virtualenv_dir"

    # pip also needs an upgrade, for some requirements (hardcoded version here for now)
    $virtualenv_dir/bin/pip install --upgrade pip==20.2.4
fi

# Now install requirements.
$virtualenv_dir/bin/pip install $pip_verbose_flag -r "$SCRIPT_DIR/requirements.txt"