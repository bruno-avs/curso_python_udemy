from typing import Type, Any
import re


class MagicalMethods:
    def __init__(
        self,
        repr: bool = False,
    ) -> None:
        self.repr = repr

    def __call__(self, cls: type[Any]) -> type[Any]:
        regex = re.compile(r"\{|\}")

        if self.repr:
            def _repr(self, *args: Any, **kwargs: Any) -> str:
                cls_name = self.__class__.__name__
                cls_dict = self.__dict__

                cls_repr = f"{cls_name}({cls_dict})"
                cls_repr = regex.sub("", cls_repr, 10)
                return cls_repr

            cls.__repr__ = _repr
        return cls
