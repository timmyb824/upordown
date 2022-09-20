import requests
import logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage/index.html')

@app.route('/website', methods=['POST'])
def website():
    URL = request.form['website']
    try:
        response = requests.head(URL)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info(f'Request sent for { URL }')
    except Exception as e:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)
        logging.error(f'Request sent for { URL } resulted in an exception: {str(e)}')
        return render_template('url/website.html', message = f"is most likely down due to: {str(e)}", url = URL)
    else:
        if response.status_code == 200:
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.info(f'Request sent for { URL } was successful')
            return render_template('url/website.html', message = "is UP!", url = URL)
        if response.status_code == 301:
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARN)
            logging.warning(f'Request sent for { URL } resulted in a {response.status_code}')
            return render_template('url/website.html', message = f"returned an HTTP response code {response.status_code}. Please try re-entering the URL with or without 'www' instead", url = URL)
        else:
            return render_template('url/website.html', message = f"may not be up due to: HTTP response code {response.status_code}", url = URL)

# app.run(host='0.0.0.0', port=5001, debug=True)
