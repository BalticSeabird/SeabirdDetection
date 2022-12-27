#!/bin/bash

set -e

IMAGE_NAME="yolov5"

ROOT_DIR=$PWD

docker run --ipc=host -it --rm --runtime nvidia \
-v $ROOT_DIR:/usr/src/seabirds \
$IMAGE_NAME \
python3 /usr/src/seabirds/export.py
