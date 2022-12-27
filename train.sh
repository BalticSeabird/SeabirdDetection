#!/bin/bash

set -e

IMAGE_NAME="yolov5"

ROOT_DIR=$PWD
#Change to fit your setup.
DATA_DIR=path-to-the_seabirddata

docker run --ipc=host -it --rm --runtime nvidia \
-v $ROOT_DIR:/usr/src/seabirds \
-v $DATA_DIR:/data:ro \
$IMAGE_NAME \
python3 /usr/src/seabirds/train.py
