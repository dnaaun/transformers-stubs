from .configuration_utils import PretrainedConfig
from .modeling_utils import PreTrainedModel
from typing import Any, Optional, Mapping

class AutoModel:
    def __init__(self) -> None: ...
    @classmethod
    def from_config(cls: Any, config: PretrainedConfig) -> PreTrainedModel: ...
    @classmethod
    def from_pretrained(
        cls: Any,
        pretrained_model_name_or_path: str,
        *model_args: Any,
        config: Optional[PretrainedConfig] = ...,
        state_dict: Optional[Mapping[str, Any]] = ...,
        cache_dir: Optional[str] = ...,
        force_download: bool = ...,
        resume_download: bool = ...,
        proxies: Optional[Mapping[str, str]] = ...,
        output_loading_info: bool = ...,
        **kwargs: Any
    ) -> PreTrainedModel: ...

class AutoModelForSequenceClassification(AutoModel):
    pass
