from dataclasses import dataclass, fields

import humps  # type: ignore


@dataclass
class _JsonresumeWrapper:
    """Parent to all classes directly resembling jsonresume data."""

    @classmethod
    def field_names(cls) -> list[str]:
        """Return the field names associated with this class."""
        return [field.name for field in fields(cls)]

    @classmethod
    def from_dict(cls, dict_data: dict) -> "_JsonresumeWrapper":
        """Construct this class from a jsonresume dict."""

        sanitized_dict_data = {}
        for field_name in cls.field_names():
            # Since the dataclass fields are in snake case and the jsonresume fields are in camel
            # case, the field names have to be camelized first.
            source_dict_key = humps.camelize(field_name)

            sanitized_dict_data[field_name] = dict_data.get(source_dict_key)

        return cls(**sanitized_dict_data)
