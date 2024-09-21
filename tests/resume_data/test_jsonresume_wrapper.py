import pytest

from resupy.resume_data import Award, Basics, Language, Location, Profile, Skill


def test_from_dict__simple():
    source_dict = {
        "language": "English",
        "fluency": "Native",
    }

    actual = Language.from_dict(source_dict)
    assert actual == Language(
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

    actual = Skill.from_dict(source_dict)
    assert actual == Skill(
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

    actual = Award.from_dict(source_dict)
    assert actual == Award(
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

    actual = Location.from_dict(source_dict)
    assert actual == Location(
        postal_code="1235",
        country_code="FR",
    )


def test_from_dict__list():
    source_dict = {
        "profiles": [
            {
                "network": "Twitter",
                "username": "xkcd",
                "url": "https://www.twitter.com",
            },
            {
                "network": "SoundCloud",
                "username": "lil programmer",
                "url": "https://soundcloud.example.com",
            },
        ]
    }

    actual = Basics.from_dict(source_dict)
    assert actual == Basics(
        profiles=[
            Profile(
                network="Twitter",
                username="xkcd",
                url="https://www.twitter.com",
            ),
            Profile(
                network="SoundCloud",
                username="lil programmer",
                url="https://soundcloud.example.com",
            ),
        ]
    )


def test_from_dict__nested_layers():
    source_dict = {
        "name": "Bilbo Baggins",
        "location": {
            "city": "Bag End",
            "region": "Hobbiton",
        },
    }

    actual = Basics.from_dict(source_dict)
    assert actual == Basics(
        name="Bilbo Baggins",
        location=Location(
            city="Bag End",
            region="Hobbiton",
        ),
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
