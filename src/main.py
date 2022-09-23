from flask import Flask, render_template, request
from helpers.logging import logger
from helpers.status_codes import url_status_code, multi_url_status_code

app = Flask(__name__)

@app.route('/')
def homepage():
    status_list = list(multi_url_status_code())
    return render_template('home/homepage.html', statuses = status_list)

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
app.run(host='0.0.0.0', port=5001)
