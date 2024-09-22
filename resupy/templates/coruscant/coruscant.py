from bs4 import BeautifulSoup

from ..template_abc import TemplateABC


class Coruscant(TemplateABC):
    """The Coruscant template."""

    def __init__(self, resume_data_dict: dict):
        """Construct this template."""

    def generate_html(self) -> BeautifulSoup:
        """Return the fully rendered HTML."""
        return BeautifulSoup()
