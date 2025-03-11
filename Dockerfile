
FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

EXPOSE 5000
ENV PYTHONUNBUFFERED=1

RUN addgroup --system appgroup && adduser --system --group appuser
USER appuser

CMD ["python", "run_app.py"]
