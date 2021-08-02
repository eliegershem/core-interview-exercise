FROM python:3.8

WORKDIR /web

ADD requirements.txt .

RUN pip3 install -r requirements.txt

ADD . .

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]