FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG_MODE=False
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get install -y postgresql-client
WORKDIR /code
RUN pip install "gunicorn>=19.8,<19.9"
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput --clear
CMD gunicorn api_cars.wsgi:application