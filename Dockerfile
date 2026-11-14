FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
