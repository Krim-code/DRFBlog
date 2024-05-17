# backend/Dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && gunicorn --bind 0.0.0.0:8000 katanaBlog.wsgi:application"]
