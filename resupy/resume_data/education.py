from dataclasses import dataclass
from typing import Optional


@dataclass
class Education:
    """Your educational history."""

    institution: str
    """The name of the institution you attended."""

    area: str
    """Your field of study like 'Arts'."""

    study_type: str
    """Like 'Bachelor', 'M.Sc.'."""

    start_date: str
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: str
    """The date the education was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    score: Optional[str]
    """Your score like '3.54/4.0'."""
