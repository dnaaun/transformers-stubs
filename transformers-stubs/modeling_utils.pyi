from torch import nn

class PreTrainedModel(nn.Module):
    base_model_prefix: str = ...
