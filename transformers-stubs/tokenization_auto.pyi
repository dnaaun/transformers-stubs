from .tokenization_utils_base import PreTrainedTokenizerBase as PreTrainedTokenizerBase
from typing import Any, Dict, Optional, overload

class AutoTokenizer:
    def __init__(self) -> None: ...
    @classmethod
    def from_pretrained(
        cls: Any,
        pretrained_model_name_or_path: str,
        *inputs: Any,
        cache_dir: Optional[str] = ...,
        force_download: bool = ...,
        resume_download: bool = ...,
        proxies: Optional[Dict[str, str]] = ...,
        use_fast: bool = ...,
        **kwargs: Any
    ) -> PreTrainedTokenizerBase: ...

__all__ = ["AutoTokenizer"]
