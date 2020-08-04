import numpy as np
from typing import Dict, NamedTuple, Optional

def is_wandb_available() -> bool: ...
def set_seed(seed: int) -> None: ...

class EvalPrediction(NamedTuple):
    predictions: np.ndarray
    label_ids: np.ndarray

class PredictionOutput(NamedTuple):
    predictions: np.ndarray
    label_ids: Optional[np.ndarray]
    metrics: Optional[Dict[str, float]]

class TrainOutput(NamedTuple):
    global_step: int
    training_loss: float
