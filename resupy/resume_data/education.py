from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Education(_JsonresumeWrapper):
    """Your educational history."""

    institution: Optional[str]
    """The name of the institution you attended."""

    url: Optional[str]
    """URL to your institution."""

    area: Optional[str]
    """Your field of study like 'Arts'."""

    study_type: Optional[str]
    """Like 'Bachelor', 'M.Sc.'."""

    start_date: Optional[str]
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: Optional[str]
    """The date the education was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    score: Optional[str]
    """Your score like '3.54/4.0'."""

    courses: Optional[list[str]]
    """List of notable courses or subjects."""
