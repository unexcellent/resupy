from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    """Your location used for sending mail."""

    address: Optional[str]
    """Your address like '1234 Glücklichkeitsstraße'."""

    postal_code: Optional[str]
    """Your postal code like '012345'."""

    city: Optional[str]
    """The name of your city."""

    country_code: Optional[str]
    """The country code as per ISO-3166-1 ALPHA-2, e.g. US, AU, IN."""

    region: Optional[str]
    """The general region where you live.

    Can be a US state, or a province, for instance.
    """
