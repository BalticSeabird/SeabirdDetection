#!/usr/bin/python3

import config
import sys

sys.path.insert(0, "/usr/src/app")

import export as yolov5_export

# Change to fit your setup.
imgsz = (384, 640)
# imgsz = (544, 960)
dataset = config.Datasets.SEABIRD1TO6
weights = "/usr/src/seabirds/models/20221227090205_seabirds_m_640.pt"


yolov5_export.run(
    data=f"/usr/src/seabirds/datadef/{dataset}",
    weights=weights,
    imgsz=imgsz,
    batch_size=1,  # 128,
    device=0,
    simplify=True,
    workspace=20,
    conf_thres=0.75,  # confidence threshold
    iou_thres=0.50,  # NMS IOU threshold
    include=[
        "engine",
    ],
)
