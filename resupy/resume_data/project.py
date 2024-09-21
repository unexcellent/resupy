from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Project(_JsonresumeWrapper):
    """Specific career projects."""

    name: Optional[str]
    """Name of the project."""

    description: Optional[str]
    """Short summary of the project.."""

    highlights: Optional[list[str]]
    """Accomplishments you had."""

    keywords: Optional[list[str]]
    """Special elements involved."""

    start_date: Optional[str]
    """The date you have started like '2014-06-29' or '2023-04' or 'Oct
    2022'."""

    end_date: Optional[str]
    """The date the project was ended like '2014-06-29' or '2023-04' or 'Oct
    2022' or 'Now' if it is still ongoing."""

    url: Optional[str]
    """URL to the project."""

    roles: Optional[list[str]]
    """Specify your roles on this project."""

    entity: Optional[str]
    """A relevant entity or organization."""

    type: Optional[str]
    """Like 'volunteering', 'presentation', 'talk', 'application',
    'conference'."""
