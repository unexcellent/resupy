from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Publication(_JsonresumeWrapper):
    """Scientific publications you have made."""

    name: Optional[str]
    """Name of the publication."""

    publisher: Optional[str]
    """Name of the publisher."""

    release_date: Optional[str]
    """The date of publication like '2014-06-29' or '2023-04' or 'Oct 2022'."""

    url: Optional[str]
    """URL to the publication."""

    summary: Optional[str]
    """A short summary of your publication."""
