import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HOMEDIR = './'
FIND_PIC = 'img'
FIND_VID = 'video'

def check_data_path(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            print(f'Error generate path {path}: {e}')

def parse_media(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pic_tags = soup.find_all(FIND_PIC)
        vid_tags = soup.find_all(FIND_VID)
        pic_count, vid_count = len(pic_tags), len(vid_tags)
        print(f'Start downloading \n{pic_count} photos and {vid_count} videos')
        return pic_count, vid_count, pic_tags + vid_tags
    else:
        raise 'Failed to fetch page!'

def download_media(url, media_tags):
        total = 0
        folder_name = url.rsplit('/', 1)[-1]
        folder_path = os.path.join(HOMEDIR, folder_name)
        check_data_path(folder_path)
        for media_tag in media_tags:
            media_url = media_tag['src']
            if media_url:
                full_media_url = urljoin(url, media_url)
                media_response = requests.get(full_media_url)
                if media_response.status_code == 200:
                    file_name = os.path.basename(media_url)
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(media_response.content)
                    total += 1
                    print(f"Downloaded: {file_name}")

        print(f'Total {total} media files successfully saved to {folder_path}')

if __name__ == '__main__':
    url = input('Enter the URL of the page: ')
    data = parse_media(url)
    download_media(url, data[2])
