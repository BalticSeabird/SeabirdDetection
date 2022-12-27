#!/usr/bin/python3

from dataclasses import dataclass


@dataclass(frozen=True)
class Yolov5Modles:
    NANO: str = "n"
    SMALL: str = "s"
    MEDIUM: str = "m"
    LARGE: str = "l"


@dataclass(frozen=True)
class Datasets:
    SEABIRD1TO6: str = "seabirds.yaml"
