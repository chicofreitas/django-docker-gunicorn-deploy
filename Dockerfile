# syntax=docker/dockerfile:1
FROM python:3


WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# EXPOSE 8000

# RUN python manage.py migrate

# CMD ["gunicorn", "--config", "gunicorn_config.py", "soucer.wsgi:application"]