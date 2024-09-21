from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


class Language(_JsonresumeWrapper):
    """A language you can speak."""

    language: Optional[str] = None
    """The name of the language like 'English', 'Spanish'."""

    fluency: Optional[str] = None
    """Your fluency level like 'B2', 'Beginner' or 'Fluent'."""
