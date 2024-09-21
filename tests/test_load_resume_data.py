from pathlib import Path

import pytest

from resupy._load_resume_data import load_resume_data
from resupy.exceptions import UnsupportedFileTypeError

# === Support methods =============================================================================


def write_to_file(content: str, path: Path) -> Path:
    """Write to a file and return its path."""

    with path.open("w") as file:
        file.write(content)

    return path


# === Test methods ================================================================================


def test_json(tmp_path):
    path = write_to_file(
        content="""
            {
                "basics": {
                    "name": "John Doe",
                    "label": "The most average person you will ever meet"
                }
            }
        """,
        path=tmp_path / "resume_data.json",
    )

    actual = load_resume_data(path)
    assert actual == {
        "basics": {"name": "John Doe", "label": "The most average person you will ever meet"}
    }


def test_json_with_comments(tmp_path):
    path = write_to_file(
        content="""
            {
                // This is a comment that normal JSON does not like
                "basics": {
                    "name": "John Doe",
                    "label": "The most average person you will ever meet"
                }
            }
        """,
        path=tmp_path / "resume_data.json",
    )

    actual = load_resume_data(path)
    assert actual == {
        "basics": {"name": "John Doe", "label": "The most average person you will ever meet"}
    }


def test_yaml(tmp_path):
    path = write_to_file(
        content="""
            basics:
                name: "John Doe"
                label: "The most average person you will ever meet"
        """,
        path=tmp_path / "resume_data.yaml",
    )

    actual = load_resume_data(path)
    assert actual == {
        "basics": {"name": "John Doe", "label": "The most average person you will ever meet"}
    }


def test_unknown_file(tmp_path):
    path = write_to_file(
        content="",
        path=tmp_path / "resume_data.UNSUPPORTED_SUFFIX",
    )

    with pytest.raises(UnsupportedFileTypeError):
        load_resume_data(path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
