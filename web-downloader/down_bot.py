import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

HOMEDIR = os.path.expanduser('~/')
FIND_DATA = ['img', 'video']

def download_media(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        media_count = 0
        folder_name = url.rsplit('/', 1)[-1]
        folder_path = os.path.join(HOMEDIR, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        media_tags = soup.find_all(FIND_DATA)
        # for i in media_tags:
        #     print(str(i) + '\n')
        # return
        for media_tag in media_tags:
            media_url = media_tag['src']
            if media_url:
                # print('media_url ' + media_url)
                full_media_url = urljoin(url, media_url)
                # print('full_media_url ' + full_media_url)
                # print(url.rsplit('/')[-1:])
                media_response = requests.get(full_media_url)
                if media_response.status_code == 200:
                    file_name = os.path.basename(media_url)
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(media_response.content)
                    media_count += 1
                    print(f"Downloaded: {file_name}")

        print(f"Total {media_count} media files downloaded to {folder_path}")
    else:
        print("Failed to fetch page!")

if __name__ == "__main__":
    url = input("Enter the URL of the page: ")
    download_media(url)
