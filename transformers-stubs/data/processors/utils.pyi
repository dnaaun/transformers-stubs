# flake8: noqa
import abc
from transformers.tokenization_utils_base import (
    PreTrainedTokenizerBase as PreTrainedTokenizerBase,
)
from typing import (
    Any,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    overload,
)
from dataclasses import dataclass
@dataclass
class InputExample:
    guid: Optional[str]
    text_a: str
    text_b: Optional[str] = ...
    label: Optional[str] = ...
    def to_json_string(self) -> str: ...
    # def __init__(self, guid: Any, text_a: Any, text_b: Any, label: Any) -> None: ...

@dataclass(frozen=True)
class InputFeatures:
    input_ids: List[int]
    attention_mask: Optional[List[int]] = ...
    token_type_ids: Optional[List[int]] = ...
    label: Optional[Union[int, float]] = ...
    def to_json_string(self) -> str: ...
    # def __init__(
    # self, input_ids: Any, attention_mask: Any, token_type_ids: Any, label: Any
    # ) -> None: ...

class DataProcessor(abc.ABC, metaclass=abc.ABCMeta):
    # @abc.abstractmethod
    # def get_example_from_tensor_dict(
    # self, tensor_dict: Mapping[Any, Any]
    # ) -> InputExample: ...
    @abc.abstractmethod
    def get_train_examples(self, data_dir: str) -> List[InputExample]: ...
    @abc.abstractmethod
    def get_dev_examples(self, data_dir: str) -> List[InputExample]: ...
    def get_test_examples(self, data_dir: str) -> List[InputExample]: ...
    @abc.abstractmethod
    def get_labels(self) -> List[str]: ...

class SingleSentenceClassificationProcessor(DataProcessor): #type: ignore
    labels: List[str]
    examples: List[InputExample]
    mode: Literal["classification", "regression"]
    verbose: bool
    def __init__(
        self,
        labels: Optional[List[str]] = None,
        examples: Optional[List[InputExample]] = None,
        mode: Literal["classification", "regression"] = "classification",
        verbose: bool = False,
    ): ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, idx: slice) -> "SingleSentenceClassificationProcessor": ...
    @overload
    def __getitem__(self, idx: int) -> InputExample: ...
    @classmethod
    def create_from_csv(
        cls,
        file_name: str,
        split_name: str = "",
        column_label: int = 0,
        column_text: int = 1,
        column_id: Optional[int] = None,
        skip_first_row: bool = False,
        **kwargs: Any,
    ) -> "SingleSentenceClassificationProcessor": ...
    @overload
    @classmethod
    def create_from_examples(
        cls,
        texts_or_text_and_labels: Sequence[str],
        labels: Sequence[str],
        **kwargs: Any,
    ) -> "SingleSentenceClassificationProcessor": ...
    @overload
    @classmethod
    def create_from_examples(
        cls,
        texts_or_text_and_labels: Sequence[Tuple[str, str]],
        labels: Literal[None] = None,
        **kwargs: Any,
    ) -> "SingleSentenceClassificationProcessor": ...
    def add_examples_from_csv(
        self,
        file_name: str,
        split_name: str = "",
        column_label: int = 0,
        column_text: int = 1,
        column_id: Optional[int] = None,
        skip_first_row: bool = False,
        overwrite_labels: bool = False,
        overwrite_examples: bool = False,
    ) -> List[InputExample]: ...
    @overload
    def add_examples(
        self,
        texts_or_text_and_labels: Sequence[Tuple[str, str]],
        labels: Literal[None] = None,
        ids: Optional[List[str]] = None,
        overwrite_labels: bool = False,
        overwrite_examples: bool = False,
    ) -> List[InputExample]: ...
    @overload
    def add_examples(
        self,
        texts_or_text_and_labels: Sequence[str],
        labels: List[str],
        ids: Optional[List[str]] = None,
        overwrite_labels: bool = False,
        overwrite_examples: bool = False,
    ) -> List[InputExample]: ... 
