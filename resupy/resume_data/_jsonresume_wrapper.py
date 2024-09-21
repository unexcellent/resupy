from dataclasses import dataclass, fields
from typing import Any

import humps  # type: ignore


@dataclass
class _JsonresumeWrapper:
    """Parent to all classes directly resembling jsonresume data."""

    @classmethod
    def fields(cls) -> dict[str, type]:
        """Return the field name and typ associated with this class."""
        return {field.name: field.type for field in fields(cls)}

    @classmethod
    def from_dict(cls, source_dict: dict) -> "_JsonresumeWrapper":
        """Construct this class from a jsonresume dict."""

        sanitized_dict_data: dict[str, Any] = {}
        for field_name, field_type in cls.fields().items():

            # All fields in the dataclasses are typing.Optional[T]. Only the type T is of interest
            # and is extracted here.
            field_class = field_type.__args__[0]  # type: ignore

            # Since the dataclass fields are in snake case and the jsonresume fields are in camel
            # case, the field names have to be camelized first.
            source_dict_key = humps.camelize(field_name)

            source_dict_does_not_contain_field = (
                source_dict_key not in source_dict or source_dict[source_dict_key] is None
            )
            if source_dict_does_not_contain_field:
                sanitized_dict_data[field_name] = None
                continue

            # If the inner class of a field has the from_dict() method, it should be constructed
            # via from_dict(). If it does not, the default constructor should be used.
            if _class_has_from_dict_method(field_class):
                sanitized_dict_data[field_name] = field_class.from_dict(source_dict[source_dict_key])
            else:
                sanitized_dict_data[field_name] = field_class(source_dict[source_dict_key])

        return cls(**sanitized_dict_data)


def _class_has_from_dict_method(cls: type) -> bool:
    """Return True if a class has a from_dict() method."""
    try:
        cls.from_dict({})  # type: ignore
    except AttributeError:
        return False
    else:
        return True
