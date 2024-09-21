from dataclasses import dataclass
from typing import Optional


@dataclass
class Reference:
    """People that can vouch for your good work."""

    name: Optional[str]
    """Name of the person you want to list as your reference."""

    reference: Optional[str]
    """The reference text."""
