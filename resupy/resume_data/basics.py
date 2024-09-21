from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper
from .location import Location
from .profile import Profile


@dataclass
class Basics(_JsonresumeWrapper):
    """Basic information about yourself."""

    name: Optional[str] = None
    """Your full name."""

    label: Optional[str] = None
    """A title you can identify with like 'Software Developer'."""

    image: Optional[str] = None
    """Path to an image of you in JPG or PNG format."""

    email: Optional[str] = None
    """Your email address."""

    phone: Optional[str] = None
    """Your phone number.

    It is stored as a string so it can be any format you like.
    """

    url: Optional[str] = None
    """URL to your website."""

    summary: Optional[str] = None
    """A short 2-3 sentence biography about yourself."""

    location: Optional[Location] = None
    """Your personal home location."""

    profiles: Optional[list[Profile]] = None
    """Your online profiles."""
