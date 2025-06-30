from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

@app.before_request
def log_request():
    logging.info(f"{request.method} {request.path} from {request.remote_addr}")

@app.route("/", methods=["GET"])
def root():
    return jsonify({"flask": "base_image"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/app", methods=["GET"])
def app_route():
    return jsonify({"test": "ok"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "path": request.path}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

