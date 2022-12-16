#!/usr/bin/python3

from dataclasses import dataclass
import sys
import time
import torch

sys.path.insert(0, "/app/yolov5")
import train as yolov5_train

assert torch.cuda.is_available()


@dataclass(frozen=True)
class Yolov5Modles:
    NANO: str = "n"
    SMALL: str = "s"
    MEDIUM: str = "m"
    LARGE: str = "l"


@dataclass(frozen=True)
class Datasets:
    SEABIRD1TO6: str = "seabirds.yaml"


timestamp = time.strftime("%Y,%m,%d,%H,%M,%S").replace(",", "")
imgsz = 640  # 960
yolov5_model = Yolov5Modles.MEDIUM
dataset = Datasets.SEABIRD1TO6
dataset_name = dataset.split(".")[0]
name = timestamp + "_" + dataset_name + "_" + yolov5_model + "_" + str(imgsz)

yolov5_train.run(
    imgsz=imgsz,
    epochs=200,
    batch_size=32,
    cfg=f"/app/yolov5/models/yolov5{yolov5_model}.yaml",
    data=f"/work/datadef/{dataset}",
    weights="",
    project="/work/runs/train",
    workers=10,
    name=name,
    patience=20,
)
