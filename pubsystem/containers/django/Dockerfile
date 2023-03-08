FROM python:3

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install git+https://github.com/neutronX/django-markdownx.git@v4.0.0-beta.1

RUN pip install -r requirements.txt

COPY . /code/