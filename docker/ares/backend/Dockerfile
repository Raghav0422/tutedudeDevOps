FROM python:3.9-alpine

ADD requirements.txt /requirements.txt

ADD a.txt /a.txt

RUN pip install -r /requirements.txt

ADD app.py /app.py

ENTRYPOINT ["python"]

CMD ["app.py"]