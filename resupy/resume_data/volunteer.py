from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Volunteer(_JsonresumeWrapper):
    """Your volunteering experience."""

    organization: Optional[str]
    """The name of the organization you volunteered for."""

    position: Optional[str]
    """The position you volunteered in."""

    url: Optional[str]
    """URL to the organization."""

    start_date: Optional[str]
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: Optional[str]
    """The date the position was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    summary: Optional[str]
    """A single sentence summary."""

    highlights: Optional[list[str]]
    """Accomplishments you had."""
