import time
from flask import Blueprint, jsonify
from app.config import START_TIME, SERVICE_NAME, VERSION

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    uptime = int(time.time() - START_TIME)

    response = {
        "status": "UP",
        "service": SERVICE_NAME,
        "version": VERSION,
        "uptime_seconds": uptime,
        "checks": {
            "application": "UP",
            "database": "UNKNOWN"
        }
    }

    return jsonify(response), 200