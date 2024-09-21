import pytest

from resupy.resume_data import Award, Language, Skill


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

    assert Skill.from_dict(dict_data) == Skill(
        name="Microsoft Excel",
        level="I can run Doom on it.",
        keywords=[
            "Office",
            "Spreadsheets",
        ],
    )


def test_from_dict__single_layer_missing_field():
    dict_data = {
        "title": "Milwaukee Hot Dog Eating Champion",
        "date": "2012-06-14",
        "awarder": "Major League Gluttony",
        # summary field is missing
    }

    assert Award.from_dict(dict_data) == Award(
        title="Milwaukee Hot Dog Eating Champion",
        date="2012-06-14",
        awarder="Major League Gluttony",
        summary=None,
    )


if __name__ == "__main__":
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])
