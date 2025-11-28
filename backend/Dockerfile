# ──────────────────────────────
# 1. Base Image
# ──────────────────────────────
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ──────────────────────────────
# 2. Set Work Directory
# ──────────────────────────────
WORKDIR /app

# ──────────────────────────────
# 3. Install System Dependencies
# ──────────────────────────────
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        wget \
        curl \
        git \
        libssl-dev \
        libffi-dev \
        && rm -rf /var/lib/apt/lists/*

# ──────────────────────────────
# 4. Copy Backend Requirements
# ──────────────────────────────
COPY requirements.txt /app/

# Upgrade pip and install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ──────────────────────────────
# 5. Copy Backend Source Code
# ──────────────────────────────
COPY ./app /app/app
COPY ./data /app/data
COPY ./scripts /app/scripts
COPY ./notebooks /app/notebooks

# ──────────────────────────────
# 6. Expose Port for FastAPI
# ──────────────────────────────
EXPOSE 8000

# ──────────────────────────────
# 7. Set Entrypoint
# ──────────────────────────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
