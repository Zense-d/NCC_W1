FROM python:3.11-alpine AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-alpine AS runner

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./app /app

ENV PATH=/root/.local/bin:$PATH

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
