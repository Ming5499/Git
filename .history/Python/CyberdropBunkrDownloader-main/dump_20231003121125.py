import requests
import json
import argparse
import sys
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse 
import requests
from tqdm import tqdm

# Define a list of image file extensions to filter
IMAGE_EXTENSIONS = ['.jpg', '.png', '.gif', '.bmp']

def get_items_list(url, custom_path=None):
    hostname = get_url_data(url)['hostname']

    r = requests.get(url, headers={'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'})
    if r.status_code != 200:
        raise Exception(f"[-] HTTP error {r.status_code}")

    soup = BeautifulSoup(r.content, 'html.parser')
    
    items = []
    
    # Check if the URL points to an album or a file
    if hostname in ['bunkr.is', 'stream.bunkr.is', 'bunkr.ru', 'stream.bunkr.ru', 'bunkr.su', 'stream.bunkr.su', 'bunkr.la', 'stream.bunkr.la', 'app.bunkr.la', 'bunkrr.su']:
        # Logic for albums
        album_name = soup.find('h1', {'class': 'text-[24px]'}).text
        album_name = remove_illegal_chars(album_name[:album_name.index('\n')] if album_name.index('\n') > 0 else album_name)
        
        boxes = soup.find_all('a', {'class': 'grid-images_box-link'})
        for box in boxes:
            item_url = box['href']
            extension = get_url_data(item_url)['extension'].lower()
            if extension in IMAGE_EXTENSIONS:
                items.append({'url': item_url, 'size': -1})

    else:
        # Logic for files
        items_dom = soup.find_all('a', {'class': 'image'})
        for item_dom in items_dom:
            item_url = item_dom['href']
            extension = get_url_data(item_url)['extension'].lower()
            if extension in IMAGE_EXTENSIONS:
                items.append({'url': item_url, 'size': -1})

    download_path = get_and_prepare_download_path(custom_path, album_name)

    for item in items:
        if 'https' not in item['url']:
            item['url'] = get_real_download_url(item['url'])
            if item['url'] is None:
                print(f"\t[-] Unable to find a download link for {item}")
                continue

        print(f"[+] Downloading {item['url']}")
        download(item['url'], download_path)

    print(f"\t[+] Download completed")
    return
    
def get_real_download_url(url):
    r = requests.get(f"https://bunkrr.su{url}")
    if r.status_code != 200:
        return f"\t[-] HTTP error {r.status_code} getting real url for {url}"
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', href=True, string=re.compile("Download")) 
    for link in links:
        return {'url': link['href'], 'size': -1}
    
    return None

def download(item_url, download_path, is_bunkr=False):
    session = create_session()

    file_name = get_url_data(item_url)['file_name']
    final_path = os.path.join(download_path, file_name)

    with session.get(item_url, stream=True) as r:
        if r.status_code != 200:
            print(f"\t[-] Error Downloading \"{file_name}\": {r.status_code}")
            return
        if r.url == "https://bnkr.b-cdn.net/maintenance.mp4":
            print(f"\t[-] Error Downloading \"{file_name}\": Server is down for maintenance")

        file_size = int(r.headers.get('content-length', -1))
        with open(final_path, 'wb') as f:
            with tqdm(total=file_size, unit='iB', unit_scale=True, desc=file_name, leave=False) as pbar:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk is not None:
                        f.write(chunk)
                        pbar.update(len(chunk))

    if is_bunkr and file_size > -1:
        downloaded_file_size = os.stat(final_path).st_size
        if downloaded_file_size != file_size:
            print(f"\t[-] {file_name} size check failed, file could be broken\n")
            return

    mark_as_downloaded(item_url, download_path)

    return

def create_session():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)',
        'Referer': 'https://bunkrr.su/'
    })
    return session

def get_url_data(url):
    parsed_url = urlparse(url)
    return {'file_name': os.path.basename(parsed_url.path), 'extension': os.path.splitext(parsed_url.path)[1], 'hostname': parsed_url.hostname}

def get_and_prepare_download_path(custom_path, album_name):

    final_path = 'downloads' if custom_path is None else custom_path
    final_path = os.path.join(final_path, album_name) if album_name is not None else 'downloads'
    final_path = final_path.replace('\n', '')

    if not os.path.isdir(final_path):
        os.makedirs(final_path)

    already_downloaded_path = os.path.join(final_path, 'already_downloaded.txt')
    if not os.path.isfile(already_downloaded_path):
        with open(already_downloaded_path, 'x', encoding='utf-8'):
            pass

    return final_path

def write_url_to_list(item_url, download_path):

    list_path = os.path.join(download_path, 'url_list.txt')

    with open(list_path, 'a', encoding='utf-8') as f:
        f.write(f"{item_url}\n")

    return

def get_already_downloaded_url(download_path):

    file_path = os.path.join(download_path, 'already_downloaded.txt')

    if not os.path.isfile(file_path):
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def mark_as_downloaded(item_url, download_path):

    file_path = os.path.join(download_path, 'already_downloaded.txt')
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"{item_url}\n")

    return


def remove_illegal_chars(string):
    return re.sub(r'[<>:"/\\|?*\']|[\0-\31]', "-", string).strip()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument("-u", help="Url to fetch", type=str, required=True)
    parser.add_argument("-e", help="Extensions to download (comma separated)", type=str)
    parser.add_argument("-p", help="Path to custom downloads folder")
    parser.add_argument("-w", help="Export url list (ex: for wget)", action="store_true")

    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    get_items_list(args.u, args.e, args.w, args.p)
