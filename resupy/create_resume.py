from pathlib import Path

from .templates import Coruscant, TemplateABC


def create_resume(
    resume_data: dict | Path,
    output_path: Path,
    template: type[TemplateABC] = Coruscant,
    quiet: bool = False,
):
    """Create a resume based on JSONResume and save it as a PDF.

    Args:
        resume_data: The data describing your resume. It needs to comply with the JSONResume schema
            (see https://jsonresume.org/). It can either be supplied as a dictionary directly or
            as a Path to either a .json or .yaml file.
        template: The template that should be used. Either a pre-defined template can be used
            (pick one from resupy.templatess) or a custom one can be used. If you created a nice
            looking template feel free to add it to the existing collection via GitHub!
        output_path: Location where the generated PDF should be outputted.
        quiet: If True, only minimal console output is produced. Defaults to False.

    # TODO: add examples
    """
