from io import BytesIO
from tests.test_health import client


def test_invalid_extension():

    response = client.post(
        "/documents/upload",

        files={
            "file": (
                "image.png",
                BytesIO(b"abc"),

                "image/png"
            )
        }
    )
    assert response.status_code == 415


def test_missing_file():

    response = client.post(
        "/documents/upload"
    )
    assert response.status_code == 422


def test_empty_filename():

    response = client.post(
        "/documents/upload",
        files={
            "file": (
                "",
                BytesIO(b"abc"),
                "application/pdf"
            )
        }
    )
    assert response.status_code == 422