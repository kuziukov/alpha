FROM python:3

COPY requirements.txt .

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt --no-cache-dir
WORKDIR /code/

COPY ./ /code/