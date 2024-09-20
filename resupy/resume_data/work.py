from dataclasses import dataclass
from typing import Optional


@dataclass
class Work:
    """Your work experience."""

    name: str
    """The name of the organization you worked for."""

    description: str
    """A description of your work there."""

    position: Optional[str]
    """The position you worked in."""

    start_date: str
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: str
    """The date the position was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    summary: Optional[str]
    """A single sentence summary."""
