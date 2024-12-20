# a script to retrieve images
from io import BytesIO
from pathlib import Path
import requests


class LocalImage():
    """Retrives images from local paths."""
    def __init__(self, path: str):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')
    

class RemoteImage():
    """Retrieves images from URLs."""
    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content) # Converts the retrived image data into bytes
    

class _LoremFlickr(RemoteImage):
    """Retrieves images from keywords."""
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))
    
    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/{self.WIDTH}/{self.HEIGHT}/{keyword}')

KeywordImage = _LoremFlickr


def ImageSource(keyword: str):
    """Returns a proper image class."""
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """Returns an image file instance."""
    return ImageSource(keyword).get_image()
