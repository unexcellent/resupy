from pathlib import Path

import pytest

from resupy._resolve_image_path import resolve_image_path


def test_same_folder(tmp_path):
    image_path = tmp_path / "profile.png"
    resume_data_path = tmp_path / "resume.yaml"

    actual = resolve_image_path("profile.png", resume_data_path)
    assert Path(actual).resolve() == image_path.resolve()


def test_neighboring_folder(tmp_path):
    image_path = tmp_path / "images" / "profile.png"
    resume_data_path = tmp_path / "resume" / "resume.yaml"

    actual = resolve_image_path("../images/profile.png", resume_data_path)
    assert Path(actual).resolve() == image_path.resolve()


def test_ignore_absolute_paths(tmp_path):
    image_path = tmp_path / "profile.png"
    resume_data_path = tmp_path / "resume.yaml"

    actual = resolve_image_path(str(image_path), resume_data_path)
    assert Path(actual).resolve() == image_path.resolve()


def test_ignore_urls(tmp_path):
    image_path = "https://example.com"
    resume_data_path = tmp_path / "resume.yaml"

    actual = resolve_image_path(image_path, resume_data_path)
    assert actual == image_path


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
