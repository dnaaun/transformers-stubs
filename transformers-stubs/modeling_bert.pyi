from transformers.modeling_outputs import BaseModelOutputWithPoolingAndCrossAttentions
from typing import Literal, Optional, Tuple, Union

from torch import Tensor

from .configuration_bert import BertConfig
from .modeling_utils import PreTrainedModel

class BertModel(PreTrainedModel):
    config: BertConfig
    def forward(
        self,
        input_ids: Optional[Tensor] = None,
        attention_mask: Optional[Tensor] = None,
        token_type_ids: Optional[Tensor] = None,
        position_ids: Optional[Tensor] = None,
        head_mask: Optional[Tensor] = None,
        inputs_embeds: Optional[Tensor] = None,
        encoder_hidden_states: Optional[Tensor] = None,
        encoder_attention_mask: Optional[Tensor] = None,
        output_hidden_states: bool = ...,
        return_dict: Literal[True]=True,
    ) -> Union[
        Tuple[Tensor, ...],
        BaseModelOutputWithPoolingAndCrossAttentions
    ]: ...
