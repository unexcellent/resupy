from dataclasses import dataclass
from typing import Optional


@dataclass
class Profile:
    """A social network you participate in."""

    network: Optional[str]
    """Name of the network like 'Facebook' or 'Github'."""

    username: Optional[str]
    """Your username."""

    url: Optional[str]
    """The URL to your profile."""
