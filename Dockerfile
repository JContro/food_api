FROM python:3.7

COPY ./app /app
COPY ./test_boto.py test_boto.py
COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN python3 test_boto.py

EXPOSE 15400

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]

