import pytest

from resupy.resume_data import (
    Award,
    Basics,
    Education,
    Interest,
    Language,
    Location,
    Profile,
    Project,
    Publication,
    Reference,
    ResumeData,
    Skill,
    Volunteer,
    Work,
)


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


def test_from_dict__wrong_field_type():
    source_dict = {"keywords": "Black Magic"}  # should be of type list[str]

    with pytest.raises(TypeError):
        Skill.from_dict(source_dict)


def test_from_dict__integration():
    source_dict = {  # source: https://github.com/jsonresume/resume-schema/blob/50798e359292ad4448d95b3bb0de5f694d6bcc4b/sample.resume.json
        "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
        "basics": {
            "name": "Richard Hendriks",
            "label": "Programmer",
            "image": "",
            "email": "richard.hendriks@mail.com",
            "phone": "(912) 555-4321",
            "url": "http://richardhendricks.example.com",
            "summary": "Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!",
            "location": {
                "address": "2712 Broadway St",
                "postalCode": "CA 94115",
                "city": "San Francisco",
                "countryCode": "US",
                "region": "California",
            },
            "profiles": [
                {
                    "network": "Twitter",
                    "username": "neutralthoughts",
                    "url": "https://www.twitter.com",
                },
                {
                    "network": "SoundCloud",
                    "username": "dandymusicnl",
                    "url": "https://soundcloud.example.com/dandymusicnl",
                },
            ],
        },
        "work": [
            {
                "name": "Pied Piper",
                "location": "Palo Alto, CA",
                "description": "Awesome compression company",
                "position": "CEO/President",
                "url": "http://piedpiper.example.com",
                "startDate": "2013-12-01",
                "endDate": "2014-12-01",
                "summary": "Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.",
                "highlights": [
                    "Build an algorithm for artist to detect if their music was violating copy right infringement laws",
                    "Successfully won Techcrunch Disrupt",
                    "Optimized an algorithm that holds the current world record for Weisman Scores",
                ],
            }
        ],
        "volunteer": [
            {
                "organization": "CoderDojo",
                "position": "Teacher",
                "url": "http://coderdojo.example.com/",
                "startDate": "2012-01-01",
                "endDate": "2013-01-01",
                "summary": "Global movement of free coding clubs for young people.",
                "highlights": ["Awarded 'Teacher of the Month'"],
            }
        ],
        "education": [
            {
                "institution": "University of Oklahoma",
                "url": "https://www.ou.edu/",
                "area": "Information Technology",
                "studyType": "Bachelor",
                "startDate": "2011-06-01",
                "endDate": "2014-01-01",
                "score": "4.0",
                "courses": ["DB1101 - Basic SQL", "CS2011 - Java Introduction"],
            }
        ],
        "awards": [
            {
                "title": "Digital Compression Pioneer Award",
                "date": "2014-11-01",
                "awarder": "Techcrunch",
                "summary": "There is no spoon.",
            }
        ],
        "publications": [
            {
                "name": "Video compression for 3d media",
                "publisher": "Hooli",
                "releaseDate": "2014-10-01",
                "url": "http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)",
                "summary": "Innovative middle-out compression algorithm that changes the way we store data.",
            }
        ],
        "skills": [
            {
                "name": "Web Development",
                "level": "Master",
                "keywords": ["HTML", "CSS", "Javascript"],
            },
            {"name": "Compression", "level": "Master", "keywords": ["Mpeg", "MP4", "GIF"]},
        ],
        "languages": [{"language": "English", "fluency": "Native speaker"}],
        "interests": [{"name": "Wildlife", "keywords": ["Ferrets", "Unicorns"]}],
        "references": [
            {
                "name": "Erlich Bachman",
                "reference": "It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.",
            }
        ],
        "projects": [
            {
                "name": "Miss Direction",
                "description": "A mapping engine that misguides you",
                "highlights": [
                    "Won award at AIHacks 2016",
                    "Built by all women team of newbie programmers",
                    "Using modern technologies such as GoogleMaps, Chrome Extension and Javascript",
                ],
                "keywords": ["GoogleMaps", "Chrome Extension", "Javascript"],
                "startDate": "2016-08-24",
                "endDate": "2016-08-24",
                "url": "http://missdirection.example.com",
                "roles": ["Team lead", "Designer"],
                "entity": "Smoogle",
                "type": "application",
            }
        ],
        "meta": {
            "canonical": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/sample.resume.json",
            "version": "v1.0.0",
            "lastModified": "2017-12-24T15:53:00",
        },
    }

    actual = ResumeData.from_dict(source_dict)
    assert actual == ResumeData(
        basics=Basics(
            name="Richard Hendriks",
            label="Programmer",
            image="",
            email="richard.hendriks@mail.com",
            phone="(912) 555-4321",
            url="http://richardhendricks.example.com",
            summary="Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!",
            location=Location(
                address="2712 Broadway St",
                postal_code="CA 94115",
                city="San Francisco",
                country_code="US",
                region="California",
            ),
            profiles=[
                Profile(
                    network="Twitter", username="neutralthoughts", url="https://www.twitter.com"
                ),
                Profile(
                    network="SoundCloud",
                    username="dandymusicnl",
                    url="https://soundcloud.example.com/dandymusicnl",
                ),
            ],
        ),
        work=[
            Work(
                name="Pied Piper",
                location="Palo Alto, CA",
                description="Awesome compression company",
                position="CEO/President",
                url="http://piedpiper.example.com",
                start_date="2013-12-01",
                end_date="2014-12-01",
                summary="Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.",
                highlights=[
                    "Build an algorithm for artist to detect if their music was violating copy right infringement laws",
                    "Successfully won Techcrunch Disrupt",
                    "Optimized an algorithm that holds the current world record for Weisman Scores",
                ],
            )
        ],
        volunteer=[
            Volunteer(
                organization="CoderDojo",
                position="Teacher",
                url="http://coderdojo.example.com/",
                start_date="2012-01-01",
                end_date="2013-01-01",
                summary="Global movement of free coding clubs for young people.",
                highlights=["Awarded 'Teacher of the Month'"],
            )
        ],
        education=[
            Education(
                institution="University of Oklahoma",
                url="https://www.ou.edu/",
                area="Information Technology",
                study_type="Bachelor",
                start_date="2011-06-01",
                end_date="2014-01-01",
                score="4.0",
                courses=["DB1101 - Basic SQL", "CS2011 - Java Introduction"],
            )
        ],
        awards=[
            Award(
                title="Digital Compression Pioneer Award",
                date="2014-11-01",
                awarder="Techcrunch",
                summary="There is no spoon.",
            )
        ],
        publications=[
            Publication(
                name="Video compression for 3d media",
                publisher="Hooli",
                release_date="2014-10-01",
                url="http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)",
                summary="Innovative middle-out compression algorithm that changes the way we store data.",
            )
        ],
        skills=[
            Skill(
                name="Web Development",
                level="Master",
                keywords=["HTML", "CSS", "Javascript"],
            ),
            Skill(name="Compression", level="Master", keywords=["Mpeg", "MP4", "GIF"]),
        ],
        languages=[Language(language="English", fluency="Native speaker")],
        interests=[Interest(name="Wildlife", keywords=["Ferrets", "Unicorns"])],
        references=[
            Reference(
                name="Erlich Bachman",
                reference="It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.",
            )
        ],
        projects=[
            Project(
                name="Miss Direction",
                description="A mapping engine that misguides you",
                highlights=[
                    "Won award at AIHacks 2016",
                    "Built by all women team of newbie programmers",
                    "Using modern technologies such as GoogleMaps, Chrome Extension and Javascript",
                ],
                keywords=["GoogleMaps", "Chrome Extension", "Javascript"],
                start_date="2016-08-24",
                end_date="2016-08-24",
                url="http://missdirection.example.com",
                roles=["Team lead", "Designer"],
                entity="Smoogle",
                type="application",
            )
        ],
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
