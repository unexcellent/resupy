from dataclasses import dataclass
from typing import Optional


@dataclass
class Skill:
    """List of your professional skill-set."""

    name: Optional[str]
    """The name of your skill like 'Cooking'."""

    level: Optional[str]
    """Descriptor of your skill-level."""

    keywords: Optional[list[str]]
    """List some keywords pertaining to this skill."""
