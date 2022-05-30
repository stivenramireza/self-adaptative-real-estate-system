FROM python:3.10.3-alpine

WORKDIR /usr/src/app

RUN python -m venv venv
RUN source venv/bin/activate

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/venv/bin/python"

ENV FLASK_APP main.py
ENV FLASK_ENV production
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
