from typing import List, Tuple, overload
from .tokenization_utils_base import PreTrainedTokenizerBase

class PreTrainedTokenizer(PreTrainedTokenizerBase):
    @overload
    def convert_tokens_to_ids(self, tokens: str) -> int: ...
    @overload
    def convert_tokens_to_ids(self, tokens: List[str]) -> List[int]: ...
    @overload
    def convert_ids_to_tokens(self, ids: int) -> str: ...
    @overload
    def convert_ids_to_tokens(
        self, ids: List[int], skip_special_tokens: bool = False
    ) -> List[str]: ...
