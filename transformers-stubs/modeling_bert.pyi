from typing import Optional, Tuple, Union, Protocol

from torch import Tensor

from .configuration_bert import BertConfig
from .modeling_utils import PreTrainedModel

class BertModel(PreTrainedModel):

    config: BertConfig
    class _forward_def(Protocol):
        def __call__(
            BertModel,
            input_ids: Optional[Tensor] = None,
            attention_mask: Optional[Tensor] = None,
            token_type_ids: Optional[Tensor] = None,
            position_ids: Optional[Tensor] = None,
            head_mask: Optional[Tensor] = None,
            inputs_embed: Optional[Tensor] = None,
            encoder_hidden_states: Optional[Tensor] = None,
            encoder_attention_mask: Optional[Tensor] = None,
        ) -> Union[
            Tuple[Tensor, Tensor],
            Tuple[Tensor, Tensor, Tensor],
            Tuple[Tensor, Tensor, Tensor, Tensor],
        ]: ...
    forward: _forward_def
    __call__: _forward_def
