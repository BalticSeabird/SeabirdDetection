#!/usr/bin/python3

import config
import sys
import time
import torch

sys.path.insert(0, "/usr/src/app")
import train as yolov5_train

assert torch.cuda.is_available()


timestamp = time.strftime("%Y,%m,%d,%H,%M,%S").replace(",", "")
imgsz = 640  # 960
yolov5_model = config.Yolov5Modles.MEDIUM
dataset = config.Datasets.SEABIRD1TO6
dataset_name = dataset.split(".")[0]
name = timestamp + "_" + dataset_name + "_" + yolov5_model + "_" + str(imgsz)

yolov5_train.run(
    imgsz=imgsz,
    epochs=200,
    batch_size=32,
    cfg=f"/usr/src/app/models/yolov5{yolov5_model}.yaml",
    data=f"/usr/src/seabirds/datadef/{dataset}",
    weights="",
    project="/usr/src/seabirds/runs/train",
    workers=10,
    name=name,
    patience=20,
)
