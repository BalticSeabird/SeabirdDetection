# Seabird Detection
This repo share scripts and code used in the [Baltic Seabird Project](http://www.balticseabird.com/).

The seabird detector is basically a wrapper around the [yolov5](https://github.com/ultralytics/yolov5) object detector.  

## Data
Note on the data...

## Get started
Clone the repo
```bash
git clone https://github.com/BalticSeabird/SeabirdDetection.git
cd SeabirdDetection
```
Build the docker image
```bash
sh build/build.sh
```

## Train
First adjust the 'DATA_DIR' in 'train.sh' to reflect your setup and set the image size and model in 'train.py'. Then start the training
```bash
sh train.sh
```

## Export
In order to improve the performance of the inference on gpu you can export the model to TensorRT
```bash
sh export.sh
```