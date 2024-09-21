class _JsonresumeWrapper:
    """Parent to all classes directly resembling jsonresume data."""

    @classmethod
    def from_dict(cls, dict_data: dict) -> "_JsonresumeWrapper":
        """Construct this class from a jsonresume dict."""
        return _JsonresumeWrapper()
