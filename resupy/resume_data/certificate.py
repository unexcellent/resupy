from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


class Certificate(_JsonresumeWrapper):
    """A certificate you have received throughout your professional career."""

    name: Optional[str] = None
    """Name of the certificate."""

    date: Optional[str] = None
    """The date you were certified like'2014-06-29' or '2023-04' or 'Oct
    2022'."""

    url: Optional[str] = None
    """URL to the issuer or certificate."""

    issuer: Optional[str] = None
    """Organization handing out the certificate."""
