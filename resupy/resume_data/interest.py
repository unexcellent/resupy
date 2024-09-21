from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Interest(_JsonresumeWrapper):
    """Any interest you would like to share."""

    name: Optional[str] = None
    """The name of your interest like 'Painting'."""

    keywords: Optional[list[str]] = None
    """Some keywords associated with the interest like 'Van Gogh'."""
