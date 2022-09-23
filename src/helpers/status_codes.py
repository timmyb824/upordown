import concurrent.futures
import requests
from helpers.settings import checkurls

def get_status_code(url, timeout = 10):
    try:
        status_code = requests.get(url, timeout = timeout).status_code
        return status_code
    except requests.ConnectionError:
        return 'UNREACHABLE'

def url_status_code(url, timeout = 10):
    try:
        if requests.get(url, timeout = timeout).status_code == 200 or 302 or 301:
            return str(get_status_code(url))
        else:
            return 'UNREACHABLE'
    except Exception:
        return 'UNREACHABLE'

def multi_url_status_code():
    statuses = {}
    temp_url_list = []
    temp_status_list = []
    for url in checkurls:
        temp_url_list.append(url)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        temp_status_list = list(executor.map(url_status_code,temp_url_list))
    for i in range(len(temp_url_list)):
        statuses[temp_url_list[i]] = temp_status_list[i]
    return statuses.items()