FROM python:3.14-slim
WORKDIR /app
RUN mkdir -p /app/data
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]