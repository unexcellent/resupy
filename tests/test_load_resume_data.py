import pytest

from resupy._load_resume_data import load_resume_data


def test_json(tmp_path):
    file_content = """
    {
        "basics": {
            "name": "John Doe",
            "label": "The most average person you will ever meet"
        }
    }"""
    path = tmp_path / "resume_data.json"

    with path.open("w") as file:
        file.write(file_content)

    actual = load_resume_data(path)
    assert actual == {
        "basics": {"name": "John Doe", "label": "The most average person you will ever meet"}
    }


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
