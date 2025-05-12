FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend/ .

# Collect static files during the build process
RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "crud_project.wsgi:application", "--bind", "0.0.0.0:8000"]
