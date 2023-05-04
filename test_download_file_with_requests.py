import os.path

import requests

def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(PROJECT_ROOT_PATH, 'resources')
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    r = requests.get(url)
    downloaded_file_path = os.path.join(path_file, 'selenium_logo.png')

    with open(downloaded_file_path, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize(downloaded_file_path)

    assert size == 30803
