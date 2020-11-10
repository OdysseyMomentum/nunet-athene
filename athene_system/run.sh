#!/bin/bash
export LC_ALL=C.UTF-8
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-7.5/lib64
source /root/anaconda3/bin/activate
source activate env_python3.4
python3.4 pipeline.py 13321
