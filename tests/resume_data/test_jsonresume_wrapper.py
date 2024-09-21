import pytest

from resupy.resume_data.language import Language


def test_from_dict__single_layer_all_fields_present():
    dict_data = {
        "language": "English",
        "fluency": "Native",
    }

    assert Language.from_dict(dict_data) == Language(
        language="English",
        fluency="Native",
    )


if __name__ == "__main__":
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])
