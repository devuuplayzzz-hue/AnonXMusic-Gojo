FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "anony"]
