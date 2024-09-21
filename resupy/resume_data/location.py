from dataclasses import dataclass
from typing import Optional

from ._jsonresume_wrapper import _JsonresumeWrapper


@dataclass
class Location(_JsonresumeWrapper):
    """Your location used for sending mail."""

    address: Optional[str]
    """Your address like '1234 Glücklichkeitsstraße'."""

    postal_code: Optional[str]
    """Your postal code like '012345'."""

    city: Optional[str]
    """The name of your city."""

    country_code: Optional[str]
    """Code as per ISO-3166-1 ALPHA-2, e.g. US, AU, IN."""

    region: Optional[str]
    """The general region where you live like 'Australia' or 'New Jersey'."""
