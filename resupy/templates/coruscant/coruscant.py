from pathlib import Path

import jinja2
from bs4 import BeautifulSoup

from ...resume_data import ResumeData
from ..template_abc import TemplateABC


class Coruscant(TemplateABC):
    """The Coruscant template."""

    INDEX_HTML_PATH = Path(__file__).parent / "index.html"

    def __init__(self, resume_data_dict: dict):
        """Construct this template."""
        self.resume_data = ResumeData.from_dict(resume_data_dict)

    def generate_html(self) -> BeautifulSoup:
        """Return the fully rendered HTML."""

        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(str(Path(__file__).parent)))
        template = environment.get_template("index.html")

        html = BeautifulSoup(template.render(resume_data=self.resume_data), "html.parser")

        return html
