#!/usr/bin/python3

import sys

sys.path.insert(0, "/app/yolov5")

import export as yolov5_export

# Change to fit your setup.
# imgsz=(384, 640)
imgsz = (544, 960)
weights = "/work/models/20221202125230_seabirds_m_960.pt"

yolov5_export.run(
    data="/work/datadef/seabirds.yaml",
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
