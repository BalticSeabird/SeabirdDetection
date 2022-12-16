#!/bin/bash

set -e

IMAGE_NAME="yolov5"

ROOT_DIR=$PWD
#Change to fit your setup.
DATA_DIR=/mnt/xdisk/data/legazy/seabirds
YOLOV5_DIR=/home/eriks/git/aiml/yolov5
#DATA_DIR=/mnt/xdisk/data/legacy/bsp/seabirds
#YOLOV5_DIR=/home/erik/git/aiml/yolov5

docker run --ipc=host -it --rm --runtime nvidia \
-v $ROOT_DIR:/work \
-v $DATA_DIR:/data:ro \
-v $YOLOV5_DIR:/app/yolov5:ro \
--user $(id -u):$(id -g) \
$IMAGE_NAME \
python3 /work/train.py
