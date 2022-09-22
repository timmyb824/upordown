import requests
import logging
from flask import Flask, render_template, request
from multiprocessing.dummy import Pool as ThreadPool

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

checkurls = {
"Websites": [
        "https://www.google.com",
        "https://www.msn.com",
        "https://doesnotexist.bbc.co.uk",
        "https://www.yahoo.com"
        ]
}

def get_status_code(url):
    try:
        status_code = requests.head(url).status_code
        return status_code
    except requests.ConnectionError:
        return 'UNREACHABLE'

def url_status_code(url):
    try:
        if requests.head(url).status_code == 200 or 302 or 301:
            return str(get_status_code(url))
        else:
            return 'UNREACHABLE'
    except Exception:
        return 'UNREACHABLE'

def multi_url_status_code():
    statuses = {}
    temp_url_list = []
    temp_status_list = []
    for group, urls in checkurls.items():
        for url in urls:
            temp_url_list.append(url)

    pool = ThreadPool(10)
    temp_status_list = pool.map(url_status_code,temp_url_list)
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
    website_check = request.form['website']
    try:
        response = requests.head(website_check)
        logger.info(f'Request sent for { website_check }')
    except Exception as e:
        logger.error(f'Request sent for { website_check } resulted in an exception: {str(e)}')
        return render_template('website/website.html', message = f"is down due to: {str(e)}", website = website_check)
    else:
        if response.status_code == 200:
            logger.info(f'Request sent for { website_check } was successful')
            return render_template('website/website.html', message = "is UP!", website = website_check)
        if response.status_code == 301:
            logger.warning(f'Request sent for { website_check } resulted in a {response.status_code}')
            return render_template('website/website.html', message = f"returned an HTTP response code {response.status_code}. Try again with or without 'www'.", website = website_check)
        else:
            return render_template('website/website.html', message = f"appears down due to: HTTP response code {response.status_code}", website = website_check)

# app.run(host='0.0.0.0', port=5001, debug=True)
