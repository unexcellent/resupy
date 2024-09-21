from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Reference(_JsonresumeWrapper):
    """People that can vouch for your good work."""

    name: Optional[str]
    """Name of the person you want to list as your reference."""

    reference: Optional[str]
    """The reference text."""
