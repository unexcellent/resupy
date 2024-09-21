from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Profile(_JsonresumeWrapper):
    """A social network you participate in."""

    network: Optional[str] = None
    """Name of the network like 'Facebook' or 'Github'."""

    username: Optional[str] = None
    """Your username."""

    url: Optional[str] = None
    """The URL to your profile."""
