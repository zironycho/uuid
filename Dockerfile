FROM python:3.6-alpine3.6

RUN pip install flask
ADD ./app.py /app/app.py

ENV FLASK_APP /app/app.py

VOLUME /data
EXPOSE 5000

CMD flask run --host=0.0.0.0
