
FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

COPY backend /app/backend

ENV PYTHONUNBUFFERED=1         PORT=8000         HOST=0.0.0.0

EXPOSE 8000

CMD ["bash", "-lc", "pip install gunicorn && gunicorn -w 2 -k gthread -b 0.0.0.0:$PORT 'backend.app:create_app'"]
