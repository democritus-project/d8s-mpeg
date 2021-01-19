import os
import sys
from typing import Iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import decorators

# TODO: may want to use the request_first_arg_url decorator for the mp4_download function and pass in a flag to return the response object rather than the url content


def mp4_download(url: str) -> Iterable[bytes]:
    """."""
    from networking import get

    result = get(url, return_response_object=True)

    for chunk in result.iter_content(chunk_size=255):
        if chunk:
            yield chunk


def mp3_download(url: str) -> Iterable[bytes]:
    return mp4_download(url)
