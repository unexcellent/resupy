from dataclasses import dataclass
from typing import Optional

from .location import Location
from .profile import Profile


@dataclass
class ResumeBasics:
    """Basic information about yourself."""

    name: str
    """Your full name."""

    label: Optional[str]
    """A title you can identify with like 'Software Developer'."""

    image: str
    """Path to an image of you in JPG or PNG format."""

    email: str
    """Your email address."""

    phone: str
    """Your phone number.

    It is stored as a string so it can be any format you like.
    """

    url: Optional[str]
    """URL to your website."""

    summary: Optional[str]
    """A short 2-3 sentence biography about yourself."""

    location: Location
    """Your personal home location."""

    profiles: Optional[list[Profile]]
    """Your social media profiles."""
