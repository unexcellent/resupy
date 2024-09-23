import abc
from pathlib import Path

from bs4 import BeautifulSoup


class TemplateABC(abc.ABC):
    """Abstract base class for all resume templates."""

    @abc.abstractmethod
    def __init__(self, resume_data_dict: dict):
        """Construct this template."""

    @abc.abstractmethod
    def generate_html(self) -> tuple[BeautifulSoup, Path]:
        """Return the fully rendered HTML."""
