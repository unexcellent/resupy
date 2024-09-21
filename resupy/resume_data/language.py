from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Language(_JsonresumeWrapper):
    """A language you can speak."""

    language: Optional[str]
    """The name of the language like 'English', 'Spanish'."""

    fluency: Optional[str]
    """Your fluency level like 'B2', 'Beginner' or 'Fluent'."""
