from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Skill(_JsonresumeWrapper):
    """List of your professional skill-set."""

    name: Optional[str] = None
    """The name of your skill like 'Cooking'."""

    level: Optional[str] = None
    """Descriptor of your skill-level."""

    keywords: Optional[list[str]] = None
    """List some keywords pertaining to this skill."""
