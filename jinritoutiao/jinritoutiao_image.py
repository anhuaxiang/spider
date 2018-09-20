import json
from threadpool import ThreadPool
from multiprocessing import Pool
import os
import logging
import requests
from hashlib import md5
from urllib.parse import urlencode


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(funcName)s - %(lineno)d -%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

base_url = 'https://www.toutiao.com/search_content/?'


def get_page(offset):
    parameters = {
        "offset": offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab",
    }
    url = base_url + urlencode(parameters)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.debug(f"请求成功 {url}")
            return response.json()
    except requests.ConnectionError:
        logger.error("连接错误")
        return None
    except requests.ConnectTimeout:
        logger.error("连接超时")
        return None


def get_images(response):
    data = response.get('data')
    if data:
        for item in data:
            title = item.get('title')
            images = item.get('image_list')
            logger.info(f'save {title}')
            if isinstance(images, list):
                for image in images:
                    yield {'title': title, 'image': image}
            yield {}


def save_iamge(item):
    title = str(item.get('title'))
    image_url = item.get('image')
    if not os.path.exists('data/' + title):
        os.mkdir('data/' + title)
    if image_url is None:
        return
    if isinstance(image_url, dict):
        image_url = r'https:' + image_url.get('url')
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            file_path = f'data/{title}/{md5(response.content).hexdigest()}.jpg'
            with open(file_path, 'wb') as f:
                f.write(response.content)
            logger.debug(f"图片{title} {image_url}请求成功")
    except requests.ConnectionError:
        logger.error(f"图片{title} {image_url}请求失败")


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        logger.info(f'保存{item}')
        save_iamge(item)


class gg(object):
    pass
if __name__ == '__main__':
    # pool = ThreadPool(5)
    pool = Pool(3)
    group = [x*20 for x in range(1, 20)]
    pool.map(main, group)
    pool.close()
    pool.join()