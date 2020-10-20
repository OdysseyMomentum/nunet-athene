#!/bin/bash

eval "$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
conda init
conda config --set restore_free_channel True
conda create -n env_python3.4 python=3.4 anaconda
source activate env_python3.4
python3.4 -m pip install -U pip
python3.4 -m pip install -r requirements.txt --upgrade
python3.4 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0rc0-cp34-cp34m-linux_x86_64.whl
