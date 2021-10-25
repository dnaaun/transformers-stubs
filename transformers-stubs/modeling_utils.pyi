from torch import nn
import torch
from torch import Tensor,  dtype as dtype_, nn
from typing_extensions import ParamSpec
from .generation_utils import GenerationMixin
from typing import Callable, Tuple, Generic, TypeVar, Type
import typing as T
from .configuration_utils import PretrainedConfig

class ModuleUtilsMixin:
    def num_parameters(self, only_trainable: bool = False) -> int: ...
    def add_memory_hooks(self) -> None: ...
    def reset_memory_hooks_state(self) -> None: ...
    @property
    def device(self) -> torch.device: ...
    @property
    def dtype(self) -> dtype_: ...
    def invert_attention_mask(self, encoder_attention_mask: Tensor) -> Tensor: ...
    def get_extended_attention_mask(
        self, attention_mask: Tensor, input_shape: Tuple, device: torch.device
    ) -> Tensor: ...

_PreTrainedConfig = TypeVar("_PreTrainedConfig", bound=PretrainedConfig)
_ForwardParams = ParamSpec("_ForwardParams")
_ForwardReturn = TypeVar("_ForwardReturn")

class MyModule(nn.Module, Generic[_ForwardParams, _ForwardReturn]):
    forward: Callable[_ForwardParams, _ForwardReturn]
    __call__: Callable[_ForwardParams, _ForwardReturn]


class PreTrainedModel(
    MyModule[_ForwardParams, _ForwardReturn],
    ModuleUtilsMixin,
    GenerationMixin,
    Generic[_ForwardParams, _ForwardReturn, _PreTrainedConfig],
):
    # Subclass type
    _PreTrainedModel = T.TypeVar("_PreTrainedModel", bound="PreTrainedModel")

    base_model_prefix: str
    config_class: T.Optional[T.Type[_PreTrainedConfig]]
    @property
    def dummy_inputs(self) -> T.Dict[str, Tensor]: ...
    def __init__(self, config: _PreTrainedConfig, *inputs: T.Any, **kwargs: T.Any): ...
    @property
    def base_model(self: _PreTrainedModel) -> T.Union[str, _PreTrainedModel]: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def set_input_embeddings(self, value: nn.Module) -> None: ...
    def get_output_embeddings(self) -> nn.Module: ...
    def tie_weights(self) -> None: ...
    def resize_token_embeddings(
        self, new_num_tokens: T.Optional[int] = None
    ) -> None: ...
    def init_weights(self) -> None: ...
    def prune_heads(self, heads_to_prune: T.Dict[int, T.List[int]]) -> None: ...
    def save_pretrained(self, save_directory: str) -> None: ...
    @classmethod
    def from_pretrained(
        cls: Type[_PreTrainedModel],
        pretrained_model_name_or_path: str,
        *model_args: T.Any,
        **kwargs: T.Any
    ) -> _PreTrainedModel: ...
