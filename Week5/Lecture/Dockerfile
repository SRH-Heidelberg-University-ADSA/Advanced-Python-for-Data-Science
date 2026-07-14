# build time---------------
FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# run time------------------------

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY app.py .
COPY model.pkl .

EXPOSE 5000

CMD ["python", "app.py"]

