from dataclasses import dataclass
from typing import Optional


@dataclass
class Interest:
    """Any interest you would like to share."""

    name: Optional[str]
    """The name of your interest like 'Painting'."""

    keywords: list[Optional[str]]
    """Some keywords associated with the interest like 'Van Gogh'."""
