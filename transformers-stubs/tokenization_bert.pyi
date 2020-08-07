from .tokenization_utils import PreTrainedTokenizer
from typing import Dict

class BertTokenizer(PreTrainedTokenizer):
    vocab: Dict[str, int]
    @property
    def vocab_size(self) -> int: ...
