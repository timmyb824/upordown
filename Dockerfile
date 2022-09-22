FROM python:3.10.0

WORKDIR /usr/src/app

COPY requirements.txt ./

# running this first will cache the packages so it does not have to run each time we change our code
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# any time there is a space in the command, we need to use the double quotes
CMD ["gunicorn", "src.main:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:5001", "--reload"]