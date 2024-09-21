from dataclasses import dataclass, fields


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
            sanitized_dict_data[field_name] = dict_data.get(field_name)

        return cls(**sanitized_dict_data)
