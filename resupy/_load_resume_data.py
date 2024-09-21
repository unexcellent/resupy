from pathlib import Path

import json5
import yaml

from .exceptions import UnsupportedFileTypeError


def load_resume_data(resume_data_path: Path) -> dict:
    """Load the resume data from a file."""

    with resume_data_path.open() as resume_data_file:

        file_is_json = resume_data_path.suffix in [".json", ".json5"]
        if file_is_json:
            return json5.load(resume_data_file)

        file_is_yaml = resume_data_path.suffix in [".yaml", ".yml"]
        if file_is_yaml:
            return yaml.load(resume_data_file, Loader=yaml.SafeLoader)

        raise UnsupportedFileTypeError(f"The file type {resume_data_path.suffix} is not supported.")
