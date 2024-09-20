from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    """Your location used for sending mail."""

    address: str
    """Your address like '1234 Glücklichkeitsstraße'."""

    postal_code: str
    """Your postal code like '012345'."""

    city: str
    """The name of your city."""

    region: Optional[str]
    """The general region where you live like 'Australia' or 'New Jersey'."""
