import pytest

from resupy.resume_data.language import Language
from resupy.resume_data.skill import Skill


def test_from_dict__single_layer_all_fields_present():
    dict_data = {
        "language": "English",
        "fluency": "Native",
    }

    assert Language.from_dict(dict_data) == Language(
        language="English",
        fluency="Native",
    )


def test_from_dict__single_layer_unexpected_field():
    dict_data = {
        "name": "Microsoft Excel",
        "level": "I can run Doom on it.",
        "keywords": [
            "Office",
            "Spreadsheets",
        ],
        "UNEXPECTED_ARGUMENT": "some_value",
    }

    with pytest.raises(TypeError):
        Skill.from_dict(dict_data)


if __name__ == "__main__":
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])
