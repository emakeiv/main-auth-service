
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 8080
ENV PYTHONUNBUFFERED=1

CMD ["python", "run_app.py"]
