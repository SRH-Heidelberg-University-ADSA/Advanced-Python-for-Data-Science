from flask import Flask, request, jsonify
import logging

# Create the Flask application.
app = Flask(__name__)


# Configure structured logging for monitoring and debugging.
logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","service":"inventory","level":"%(levelname)s","message":"%(message)s"}'
)

# Create a logger for this microservice.
logger = logging.getLogger("inventory_service")


# Simulated inventory database.
# In a real system, this data would usually be stored in a database.
stock = {
    "book_001": 5,
    "book_002": 0,
    "book_003": 12,
}


@app.route("/check_stock", methods=["POST"])
def check_stock():
    # Receive the order information sent by the Order Service.
    data = request.get_json(silent=True)

    # Validate that the request contains the required fields.
    if not data or "book_id" not in data or "quantity" not in data:
        logger.warning("rejected malformed stock check request")
        return jsonify({"error": "book_id and quantity are required"}), 400

    # Extract book identifier and requested quantity.
    book_id = data["book_id"]
    quantity = data["quantity"]

    # Retrieve the current stock level.
    # Return 0 if the requested book does not exist.
    available = stock.get(book_id, 0)


    # Check whether enough items are available.
    if available >= quantity:

        # Reduce the inventory after approving the order.
        stock[book_id] -= quantity

        # Log successful stock reservation.
        logger.info(
            f"book_id={book_id} qty={quantity} approved, "
            f"{stock[book_id]} left"
        )

        # Return a successful stock confirmation response.
        return jsonify({
            "in_stock": True,
            "remaining": stock[book_id]
        }), 200


    else:
        # Log failed stock validation.
        logger.info(
            f"book_id={book_id} qty={quantity} denied, "
            f"only {available} left"
        )

        # Inform the Order Service that the item is unavailable.
        return jsonify({
            "in_stock": False,
            "remaining": available
        }), 200



@app.route("/health", methods=["GET"])
def health():
    # Health endpoint used by monitoring tools and Kubernetes probes.
    return jsonify({
        "status": "ok",
        "service": "inventory_service"
    }), 200



if __name__ == "__main__":
    # Start the Inventory Service on port 5001.
    app.run(host="0.0.0.0", port=5001, debug=False)
