FROM python:3.7

ENV POSTGRES_DB spacex
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD admin

# Install Postgres
RUN apt-get update && apt-get install -y postgresql-client-13 python3-requests

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy source code
COPY . /app

# Set working directory
WORKDIR /app

# make wait-for-postgres.sh executable
RUN chmod +x ./cmd/wait-for-postgres.sh

# CMD ["python", "create_db.py"]

# CMD ["python", "create_views.py"]

# CMD ["python", "script.py"]