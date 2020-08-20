from typing import (
    Union,
    Dict,
    List,
    Any,
    Optional,
    Sequence,
    overload,
    Tuple,
)

from tokenizers import Encoding as EncodingFast
from collections import UserDict
from enum import Enum

TextInput = str
PreTokenizedInput = List[str]
EncodedInput = List[int]
TextInputPair = Tuple[str, str]
PreTokenizedInputPair = Tuple[List[str], List[str]]
EncodedInputPair = Tuple[List[int], List[int]]

class ExplicitEnum(Enum):
    @classmethod
    def _missing_(cls, value: Any) -> None: ...

class TruncationStrategy(ExplicitEnum):
    ONLY_FIRST: str
    ONLY_SECOND: str
    LONGEST_FIRST: str
    DO_NOT_TRUNCATE: str

class PaddingStrategy(ExplicitEnum):
    LONGEST: str
    MAX_LENGTH: str
    DO_NOT_PAD: str

class TensorType(ExplicitEnum):
    PYTORCH: str
    TENSORFLOW: str
    NUMPY: str

class BatchEncoding(UserDict[str, Any]):
    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        encoding: Optional[Union[EncodingFast, Sequence[EncodingFast]]] = None,
        tensor_type: Union[None, str, TensorType] = None,
        prepend_batch_axis: bool = False,
    ): ...
    @property
    def is_fast(self) -> bool: ...
    @overload
    def __getitem__(self, item: str) -> Any: ...
    @overload
    def __getitem__(self, item: int) -> EncodingFast: ...
    def __getattr__(self, item: str) -> Any: ...
    def __getstate__(self) -> Dict[str, Any]: ...
    def __setstate__(self, state: Dict[str, Any]) -> None: ...
    @property
    def encodings(self) -> Optional[List[EncodingFast]]: ...
    def tokens(self, batch_index: int = 0) -> List[str]: ...
    def words(self, batch_index: int = 0) -> List[Optional[int]]: ...
    def token_to_word(
        self, batch_or_token_index: int, token_index: Optional[int] = None
    ) -> int: ...

#    def word_to_tokens(
#        self, batch_or_word_index: int, word_index: Optional[int] = None
#    ) -> TokenSpan: ...
#    def token_to_chars(
#        self, batch_or_token_index: int, token_index: Optional[int] = None
#    ) -> CharSpan: ...
#    def char_to_token(
#        self, batch_or_char_index: int, char_index: Optional[int] = None
#    ) -> int: ...
#    def word_to_chars(
#        self, batch_or_word_index: int, word_index: Optional[int] = None
#    ) -> CharSpan: ...
#    def char_to_word(
#        self, batch_or_char_index: int, char_index: Optional[int] = None
#    ) -> int: ...
#    def convert_to_tensors(
#        self,
#        tensor_type: Optional[Union[str, TensorType]] = None,
#        prepend_batch_axis: bool = False,
#    ): ...
#    @torch_required
#    def to(self, device: str) -> "BatchEncoding": ...

class SpecialTokensMixin:
    def __init__(self, verbose: bool = ...) -> None: ...
    @property
    def bos_token(self) -> str: ...
    @property
    def eos_token(self) -> str: ...
    @property
    def unk_token(self) -> str: ...
    @property
    def sep_token(self) -> str: ...
    @property
    def pad_token(self) -> str: ...
    @property
    def cls_token(self) -> str: ...
    @property
    def mask_token(self) -> str: ...

class PreTrainedTokenizerBase(SpecialTokensMixin):
    @property
    def max_len(self) -> int: ...
    def __call__(
        self,
        text: Union[
            TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]
        ],
        text_pair: Optional[
            Union[
                TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]
            ]
        ] = None,
        add_special_tokens: bool = True,
        padding: Union[bool, str, PaddingStrategy] = False,
        truncation: Union[bool, str, TruncationStrategy] = False,
        max_length: Optional[int] = None,
        stride: int = 0,
        is_pretokenized: bool = False,
        pad_to_multiple_of: Optional[int] = None,
        return_tensors: Optional[Union[str, TensorType]] = None,
        return_token_type_ids: Optional[bool] = None,
        return_attention_mask: Optional[bool] = None,
        return_overflowing_tokens: bool = False,
        return_special_tokens_mask: bool = False,
        return_offsets_mapping: bool = False,
        return_length: bool = False,
        verbose: bool = True,
        **kwargs: Any
    ) -> BatchEncoding: ...
    def save_pretrained(self, save_directory: str) -> Tuple[str, ...]: ...
    def encode(
        self,
        text: Union[TextInput, PreTokenizedInput, EncodedInput],
        text_pair: Optional[Union[TextInput, PreTokenizedInput, EncodedInput]] = None,
        add_special_tokens: bool = True,
        padding: Union[bool, str, PaddingStrategy] = False,
        truncation: Union[bool, str, TruncationStrategy] = False,
        max_length: Optional[int] = None,
        stride: int = 0,
        return_tensors: Optional[Union[str, TensorType]] = None,
        **kwargs: Any
    ) -> List[int]: ...
