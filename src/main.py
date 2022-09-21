import requests
import logging
from flask import Flask, render_template, request, redirect, url_for

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    CHECK = 'https://gitea.local.timmybtech.com'
    try:
        response = requests.head(CHECK)
        logger.info(f'Check sent for { CHECK }')
    except Exception as e:
        return render_template('homepage/index.html', check = CHECK, message = 'EXCEPTION!')
    else:
        if response.status_code == 200:
            return render_template('homepage/index.html', check = CHECK, message = 'UP!')
        if response.status_code == 301:
            return render_template('homepage/index.html', check = CHECK, message = 'Moved Permenantly')
        else:
            return render_template('homepage/index.html', check = CHECK, message = 'DOWN!')

@app.route('/website', methods=['POST'])
def website():
    URL = request.form['website']
    try:
        response = requests.head(URL)
        logger.info(f'Request sent for { URL }')
    except Exception as e:
        logger.error(f'Request sent for { URL } resulted in an exception: {str(e)}')
        return render_template('url/website.html', message = f"is down due to: {str(e)}", url = URL)
    else:
        if response.status_code == 200:
            logger.info(f'Request sent for { URL } was successful')
            return render_template('url/website.html', message = "is UP!", url = URL)
        if response.status_code == 301:
            logger.warning(f'Request sent for { URL } resulted in a {response.status_code}')
            return render_template('url/website.html', message = f"returned an HTTP response code {response.status_code}. Try again with or without 'www'.", url = URL)
        else:
            return render_template('url/website.html', message = f"appears down due to: HTTP response code {response.status_code}", url = URL)

# app.run(host='0.0.0.0', port=5001, debug=True)
