from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


class Reference(_JsonresumeWrapper):
    """People that can vouch for your good work."""

    name: Optional[str] = None
    """Name of the person you want to list as your reference."""

    reference: Optional[str] = None
    """The reference text."""
