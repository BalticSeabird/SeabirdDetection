#!/bin/bash

set -e

IMAGE_NAME="yolov5"

docker build -f Dockerfile -t $IMAGE_NAME .
