# Jupyter Notebook magic command: Writes all code in this cell into a Python file named order_service.py
# This allows us to create a standalone microservice file from the notebook.
"""
Order Service
This microservice receives book orders, validates incoming requests, and communicates with the Inventory Service to check product availability.
The example demonstrates key microservice concepts, including API endpoints, service-to-service communication, logging, security checks, and monitoring.
"""
from flask import Flask, request, jsonify
import requests
import logging
import time
import uuid
import os

app = Flask(__name__)

# Configure structured logging for monitoring.
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","service":"order","level":"%(levelname)s","message":"%(message)s"}'
)
logger = logging.getLogger("order_service")

# Inventory service URL from environment variable.
INVENTORY_SERVICE_URL = os.environ.get("INVENTORY_SERVICE_URL", "http://localhost:5001")

# Demo API key for request authentication.
API_KEY = "week7-secret-key"

# Simple application metrics.
metrics = {
    "requests_received": 0,
    "orders_placed": 0,
    "orders_rejected": 0,
    "total_response_time": 0.0,
}


def require_api_key(req):
    """Validate the API key in the request header."""
    return req.headers.get("X-API-Key") == API_KEY


@app.route("/order", methods=["POST"])
def place_order():
    start_time = time.time()
    metrics["requests_received"] += 1

    # Generate unique ID for request tracing.
    request_id = str(uuid.uuid4())[:8]

    # Check request authentication.
    if not require_api_key(request):
        logger.warning(f"[{request_id}] invalid API key")
        metrics["orders_rejected"] += 1
        return jsonify({"error": "invalid API key"}), 401

    # Read request JSON payload.
    data = request.get_json(silent=True)

    # Validate required fields.
    if not data or "book_id" not in data or "quantity" not in data:
        logger.warning(f"[{request_id}] invalid payload")
        metrics["orders_rejected"] += 1
        return jsonify({"error": "order must include book_id and quantity"}), 400

    # Validate order quantity.
    if not isinstance(data["quantity"], int) or data["quantity"] <= 0:
        logger.warning(f"[{request_id}] invalid quantity")
        metrics["orders_rejected"] += 1
        return jsonify({"error": "quantity must be a positive integer"}), 400

    logger.info(f"[{request_id}] processing order")

    # Request stock information from inventory service.
    try:
        response = requests.post(
            f"{INVENTORY_SERVICE_URL}/check_stock",
            json={
                "book_id": data["book_id"],
                "quantity": data["quantity"]
            },
            timeout=3,
        )
        stock_result = response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"[{request_id}] inventory unavailable: {e}")
        return jsonify({"error": "inventory service unavailable"}), 503

    # Measure response time.
    elapsed = time.time() - start_time
    metrics["total_response_time"] += elapsed

    # Confirm order if stock is available.
    if stock_result.get("in_stock"):
        metrics["orders_placed"] += 1
        logger.info(f"[{request_id}] order confirmed")

        return jsonify({
            "request_id": request_id,
            "status": "confirmed",
            "book_id": data["book_id"],
            "quantity": data["quantity"],
        }), 201

    # Reject order if stock is unavailable.
    metrics["orders_rejected"] += 1
    logger.info(f"[{request_id}] out of stock")

    return jsonify({
        "request_id": request_id,
        "status": "out_of_stock",
        "book_id": data["book_id"],
    }), 409


@app.route("/health", methods=["GET"])
def health():
    # Health check endpoint for monitoring.
    return jsonify({"status": "ok", "service": "order_service"}), 200


@app.route("/metrics", methods=["GET"])
def get_metrics():
    # Calculate average successful request time.
    avg_time = (
        metrics["total_response_time"] / metrics["orders_placed"]
        if metrics["orders_placed"] > 0 else 0
    )

    return jsonify({
        "requests_received": metrics["requests_received"],
        "orders_placed": metrics["orders_placed"],
        "orders_rejected": metrics["orders_rejected"],
        "average_response_time_seconds": round(avg_time, 4),
    }), 200


if __name__ == "__main__":
    # Start Flask service.
    app.run(host="0.0.0.0", port=5000, debug=False)

