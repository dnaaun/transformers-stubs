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
    pass
