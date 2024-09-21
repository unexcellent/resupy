from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper
from .award import Award
from .basics import Basics
from .certificate import Certificate
from .education import Education
from .interest import Interest
from .language import Language
from .project import Project
from .publication import Publication
from .reference import Reference
from .skill import Skill
from .volunteer import Volunteer
from .work import Work


@dataclass
class ResumeData(_JsonresumeWrapper):
    """Root data container of resume data."""

    basics: Optional[Basics]
    """Basic information about yourself."""

    work: Optional[list[Work]]
    """Your job positions."""

    volunteer: Optional[list[Volunteer]]
    """Your volunteering experience."""

    education: Optional[list[Education]]
    """Your educational history."""

    awards: Optional[list[Award]]
    """Awards you have received."""

    certificates: Optional[list[Certificate]]
    """Certificates you have received."""

    publications: Optional[list[Publication]]
    """Any publications you have made."""

    skills: Optional[list[Skill]]
    """Your professional skills."""

    languages: Optional[list[Language]]
    """The languages you know."""

    interests: Optional[list[Interest]]
    """Your private interests."""

    references: Optional[list[Reference]]
    """Any references you want to list."""

    projects: Optional[list[Project]]
    """Specific career projects."""
