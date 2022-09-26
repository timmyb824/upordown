from flask import Flask, render_template, request
from src.upordown.status_codes import url_status_code, multi_url_status_code
import logging, logging.config
# import traceback
from datetime import datetime
from pytz import timezone

logging.config.fileConfig('./src/upordown/configs/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def homepage():
    status_list = list(multi_url_status_code())
    logger.info(f'Request sent for { status_list }')
    tz = timezone('America/New_York')
    now = datetime.now(tz)
    last_updated = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('home/homepage.html', statuses = status_list, time = last_updated)

@app.route('/website', methods=['POST'])
def website():
    website = request.form['website']
    website_check = url_status_code(request.form['website'])
    logger.info(f'Request sent for { website } and returned status: { website_check }')
    if website_check != 'UNREACHABLE':
        return render_template('website/website.html', website = website, message = "UP!")
    else:
        return render_template('website/website.html', website = website, message = website_check)

# add `debug=True` for debugging purposes
# app.run(host='0.0.0.0', port=5001)
