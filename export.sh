#!/bin/bash

set -e

IMAGE_NAME="yolov5"

ROOT_DIR=$PWD
#Change to fit your setup.
YOLOV5_DIR=/home/eriks/git/aiml/yolov5

docker run --ipc=host -it --rm --runtime nvidia \
-v $ROOT_DIR:/work \
-v $YOLOV5_DIR:/app/yolov5:ro \
--user $(id -u):$(id -g) \
$IMAGE_NAME \
python3 /work/export.py
