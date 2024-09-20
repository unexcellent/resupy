from dataclasses import dataclass
from typing import Optional

from .location import Location
from .profile import Profile


@dataclass
class Basics:
    """Basic information about yourself."""

    name: Optional[str]
    """Your full name."""

    label: Optional[str]
    """A title you can identify with like 'Software Developer'."""

    image: Optional[str]
    """Path to an image of you in JPG or PNG format."""

    email: Optional[str]
    """Your email address."""

    phone: Optional[str]
    """Your phone number.

    It is stored as a string so it can be any format you like.
    """

    url: Optional[str]
    """URL to your website."""

    summary: Optional[str]
    """A short 2-3 sentence biography about yourself."""

    location: Optional[Location]
    """Your personal home location."""

    profiles: Optional[list[Profile]]
    """Your online profiles."""
