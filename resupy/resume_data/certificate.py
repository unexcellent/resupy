from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Certificate(_JsonresumeWrapper):
    """A certificate you have received throughout your professional career."""

    name: Optional[str]
    """Name of the certificate."""

    date: Optional[str]
    """The date you were certified like'2014-06-29' or '2023-04' or 'Oct
    2022'."""

    url: Optional[str]
    """URL to the issuer or certificate."""

    issuer: Optional[str]
    """Organization handing out the certificate."""
