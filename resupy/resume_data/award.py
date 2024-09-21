from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Award(_JsonresumeWrapper):
    """An award you have received throughout your professional career."""

    title: Optional[str]
    """Title of the award."""

    date: Optional[str]
    """The date you were awarded like'2014-06-29' or '2023-04' or 'Oct
    2022'."""

    awarder: Optional[str]
    """Organization handing out the award."""

    summary: Optional[str]
    """Short summary of why it was awarded."""
