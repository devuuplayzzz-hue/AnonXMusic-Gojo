FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    git \
    unzip \
    && curl -fsSL https://deno.land/x/install/install.sh | sh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV DENO_INSTALL="/root/.deno"
ENV PATH="$DENO_INSTALL/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "anony"]
