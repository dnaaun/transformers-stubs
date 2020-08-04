from typing import Any, Dict, Literal, Optional, Tuple, overload
from .configuration_utils import PretrainedConfig

class AutoConfig:
    def __init__(self) -> None: ...
    @overload
    @classmethod
    def from_pretrained(
        cls: Any,
        pretrained_model_name_or_path: str,
        return_unused_kwargs: Literal[True],
        *,
        cache_dir: Optional[str] = ...,
        force_download: bool = ...,
        resume_download: bool = ...,
        proxies: Optional[Dict[str, str]] = ...,
        **kwargs: Any
    ) -> Tuple[PretrainedConfig, Dict[str, str]]: ...
    @overload
    @classmethod
    def from_pretrained(
        cls: Any,
        pretrained_model_name_or_path: str,
        *,
        return_unused_kwargs: Literal[False] = ...,
        cache_dir: Optional[str] = ...,
        force_download: bool = ...,
        resume_download: bool = ...,
        proxies: Optional[Dict[str, str]] = ...,
        **kwargs: Any
    ) -> PretrainedConfig: ...

__all__ = ["AutoConfig"]
