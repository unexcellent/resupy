from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Work(_JsonresumeWrapper):
    """Your work experience."""

    name: Optional[str] = None
    """The name of the organization you worked for."""

    location: Optional[str] = None
    """Location of your work like 'New York City'."""

    description: Optional[str] = None
    """A description of your work there."""

    position: Optional[str] = None
    """The position you worked in."""

    url: Optional[str] = None
    """URL to the employer."""

    start_date: Optional[str] = None
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: Optional[str] = None
    """The date the position was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    summary: Optional[str] = None
    """A single sentence summary."""

    highlights: Optional[list[str]] = None
    """Accomplishments you had like 'Increased profits by 20% through social
    media marketing'."""
