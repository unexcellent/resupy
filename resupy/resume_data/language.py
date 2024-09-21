from dataclasses import dataclass
from typing import Optional


@dataclass
class Language:
    """A language you can speak."""

    language: Optional[str]
    """The name of the language like 'English', 'Spanish'."""

    fluency: Optional[str]
    """Your fluency level like 'B2', 'Beginner' or 'Fluent'."""
