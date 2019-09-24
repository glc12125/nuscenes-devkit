"""
This code is based on Xinshuo Weng's AB3DMOT code at:
https://github.com/xinshuoweng/AB3DMOT/blob/master/evaluation/evaluate_kitti3dmot.py
"""

import numpy as np

from nuscenes.eval.common.data_classes import EvalBoxes
from nuscenes.eval.tracking.data_classes import TrackingMetricData


def accumulate(gt_boxes: EvalBoxes,
               pred_boxes: EvalBoxes,
               class_name: str,
               dist_fcn_name: str,
               dist_th: float,
               verbose: bool = False) -> TrackingMetricData:
    pass  # TODO


def calc_all_metrics():
    pass


def get_score_ths(n: int = 11) -> np.array:
    """
    Returns the recall thresholds.
    :param n:
    :return:
    """
    score_ths = np.linspace(0, 1, n)[1:]  # TODO
    return score_ths
