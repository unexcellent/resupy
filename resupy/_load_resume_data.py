from pathlib import Path

import json5


def load_resume_data(resume_data_path: Path) -> dict:
    """Load the resume data from a file."""

    with resume_data_path.open() as resume_data_file:
        resume_data = json5.load(resume_data_file)

    return resume_data
