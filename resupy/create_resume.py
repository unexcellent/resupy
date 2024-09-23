from pathlib import Path

import pdfkit

from ._load_resume_data import load_resume_data
from .templates import Coruscant, TemplateABC


def create_resume(
    resume_data: dict | Path,
    output_path: Path,
    template_class: type[TemplateABC] = Coruscant,
):
    """Create a resume based on JSONResume and save it as a PDF.

    Args:
        resume_data: The data describing your resume. It needs to comply with the JSONResume schema
            (see https://jsonresume.org/). It can either be supplied as a dictionary directly or
            as a Path to either a .json or .yaml file.
        template_class: The template that should be used. Either a pre-defined template can be used
            (pick one from resupy.templatess) or a custom one can be used. If you created a nice
            looking template feel free to add it to the existing collection via GitHub!
        output_path: Location where the generated PDF should be outputted.

    # TODO: add examples
    """
    if isinstance(resume_data, Path):
        resume_data_dict = load_resume_data(resume_data)
    else:
        resume_data_dict = resume_data

    template = template_class(resume_data_dict)
    html_resume, css_path = template.generate_html()

    _write_pdf(html_resume.prettify(), css_path, output_path)


def _write_pdf(html_string: str, css_path: Path, output_path: Path):
    pdfkit.from_string(
        html_string,
        str(output_path),
        options={
            "--margin-top": "0",
            "--margin-bottom": "0",
            "--margin-left": "0",
            "--margin-right": "0",
            "--title": "Resume",
            "--enable-local-file-access": True,
        },
        css=str(css_path),
    )
