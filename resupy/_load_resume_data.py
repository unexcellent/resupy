import json
from pathlib import Path


def load_resume_data(resume_data_path: Path) -> dict:
    """Load the resume data from a file."""

    with resume_data_path.open() as resume_data_file:
        resume_data = json.load(resume_data_file)

    return resume_data
