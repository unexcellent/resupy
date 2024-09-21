import humps
import pydantic


class _JsonresumeWrapper(pydantic.BaseModel):
    """Parent to all classes directly resembling jsonresume data."""

    @classmethod
    def from_dict(cls, source_dict: dict) -> "_JsonresumeWrapper":
        """Construct this class from a jsonresume dict."""

        # Since the class are in snake case and the jsonresume fields are in camel
        # case, the field names have to be decamelized first.
        sanatized_source_dict = humps.decamelize(source_dict)

        return cls(**sanatized_source_dict)
