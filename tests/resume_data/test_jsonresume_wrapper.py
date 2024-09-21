import pytest

from resupy.resume_data import Award, Language, Location, Skill


def test_from_dict__simple():
    dict_data = {
        "language": "English",
        "fluency": "Native",
    }

    assert Language.from_dict(dict_data) == Language(
        language="English",
        fluency="Native",
    )


def test_from_dict__unexpected_field():
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


def test_from_dict__missing_field():
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


def test_from_dict__camel_case_to_snake_case():
    dict_data = {
        "postalCode": "1235",
        "countryCode": "FR",
    }

    assert Location.from_dict(dict_data) == Location(
        postal_code="1235",
        country_code="FR",
    )


if __name__ == "__main__":
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])
