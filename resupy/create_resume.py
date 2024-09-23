from pathlib import Path

import pdfkit

from ._load_resume_data import load_resume_data
from ._resolve_image_path import resolve_image_path
from .templates import Coruscant, TemplateABC


def create_resume(
    resume_data_path: Path,
    output_path: Path,
    template_class: type[TemplateABC] = Coruscant,
):
    """Create a resume based on JSONResume and save it as a PDF.

    Args:
        resume_data_path: Path to the data describing your resume. It needs to comply with the
            JSONResume schema (see https://jsonresume.org/).
        template_class: The template that should be used. Either a pre-defined template can be used
            (pick one from resupy.templatess) or a custom one can be used. If you created a nice
            looking template feel free to add it to the existing collection via GitHub!
        output_path: Location where the generated PDF should be outputted.

    # TODO: add examples
    """
    resume_data_dict = load_resume_data(resume_data_path)

    if resume_data_dict["basics"]["image"] is not None:
        resume_data_dict["basics"]["image"] = resolve_image_path(
            resume_data_dict["basics"]["image"], resume_data_path
        )

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
