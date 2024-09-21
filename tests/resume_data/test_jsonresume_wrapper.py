import pytest

from resupy.resume_data import Award, Basics, Language, Location, Skill


def test_from_dict__simple():
    source_dict = {
        "language": "English",
        "fluency": "Native",
    }

    assert Language.from_dict(source_dict) == Language(
        language="English",
        fluency="Native",
    )


def test_from_dict__unexpected_field():
    source_dict = {
        "name": "Microsoft Excel",
        "level": "I can run Doom on it.",
        "keywords": [
            "Office",
            "Spreadsheets",
        ],
        "UNEXPECTED_ARGUMENT": "some_value",
    }

    assert Skill.from_dict(source_dict) == Skill(
        name="Microsoft Excel",
        level="I can run Doom on it.",
        keywords=[
            "Office",
            "Spreadsheets",
        ],
    )


def test_from_dict__missing_field():
    source_dict = {
        "title": "Milwaukee Hot Dog Eating Champion",
        "date": "2012-06-14",
        "awarder": "Major League Gluttony",
        # summary field is missing
    }

    assert Award.from_dict(source_dict) == Award(
        title="Milwaukee Hot Dog Eating Champion",
        date="2012-06-14",
        awarder="Major League Gluttony",
        summary=None,
    )


def test_from_dict__camel_case_to_snake_case():
    source_dict = {
        "postalCode": "1235",
        "countryCode": "FR",
    }

    assert Location.from_dict(source_dict) == Location(
        postal_code="1235",
        country_code="FR",
    )


def test_from_dict__nested_layers():
    source_dict = {
        "name": "Bilbo Baggins",
        "location": {
            "city": "Bag End",
            "region": "Hobbiton",
        },
    }

    assert Basics.from_dict(source_dict) == Basics(
        name="Bilbo Baggins",
        location=Location(
            city="Bag End",
            region="Hobbiton",
        ),
    )


if __name__ == "__main__":
    pytest.main([__file__, "--disable-pytest-warnings", "--cache-clear", "-v"])
