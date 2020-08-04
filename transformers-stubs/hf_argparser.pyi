from argparse import ArgumentParser, Namespace
from typing import (
    Any,
    Iterable,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
    overload,
    Protocol,
)

class DataClassProtocol(Protocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HfArgumentParser(ArgumentParser):
    dataclass_types: Iterable[Type[DataClassProtocol]]
    def __init__(
        self,
        dataclass_types: Union[
            Type[DataClassProtocol], Iterable[Type[DataClassProtocol]]
        ],
        **kwargs: Any
    ) -> None: ...
    @overload
    def parse_args_into_dataclasses(
        self,
        return_remaining_strings: Literal[False],
        *,
        args: Optional[List[str]] = ...,
        look_for_args_file: bool = ...
    ) -> Tuple[Union[Namespace, DataClassProtocol], ...]: ...
    @overload
    def parse_args_into_dataclasses(
        self,
        return_remaining_strings: Literal[True],
        *,
        args: Optional[List[str]] = ...,
        look_for_args_file: bool = ...
    ) -> Tuple[Union[Namespace, List[str], DataClassProtocol], ...]: ...
    @overload
    def parse_args_into_dataclasses(
        self, *, args: Optional[List[str]] = ..., look_for_args_file: bool = ...
    ) -> Tuple[Union[Namespace, DataClassProtocol], ...]: ...
    def parse_json_file(self, json_file: str) -> Tuple[DataClassProtocol, ...]: ...
    def parse_dict(self, args: dict) -> Tuple[DataClassProtocol, ...]: ...
