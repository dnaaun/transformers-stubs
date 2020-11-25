from .tokenization_utils import PreTrainedTokenizer
from .tokenization_utils_fast import PreTrainedTokenizerFast
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
    ) -> Union[PreTrainedTokenizer, PreTrainedTokenizerFast]: ...

__all__ = ["AutoTokenizer"]
