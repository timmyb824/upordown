import requests
import logging
from flask import Flask, render_template, request
import concurrent.futures

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

checkurls = [
        "https://www.google.com",
        "https://www.msn.com",
        "https://doesnotexist.bbc.co.uk",
        "https://www.yahoo.com"
]

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

app = Flask(__name__)

@app.route('/')
def homepage():
    status_list = list(multi_url_status_code())
    return render_template('home/homepage.html', statuses = status_list, checkurls = checkurls)

@app.route('/website', methods=['POST'])
def website():
    website = request.form['website']
    website_check = url_status_code(request.form['website'])
    if website_check != 'UNREACHABLE':
        return render_template('website/website.html', website = website, message = "UP!")
    else:
        return render_template('website/website.html', website = website, message = website_check)

# app.run(host='0.0.0.0', port=5001, debug=True)
