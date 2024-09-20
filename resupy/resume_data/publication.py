from dataclasses import dataclass
from typing import Optional


@dataclass
class Publication:
    """Scientific publications you have made."""

    name: str
    """Name of the publication."""

    publisher: str
    """Name of the publisher."""

    release_date: str
    """The date of publication like '2014-06-29' or '2023-04' or 'Oct 2022'."""

    url: Optional[str]
    """URL to the publication."""

    summary: str
    """A short summary of your publication."""
