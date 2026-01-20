from flask import Flask
import sys

print("Starting Flask app...", file=sys.stderr, flush=True)

try:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello from Jenkins Python Pipeline!"

    if __name__ == "__main__":
        print("Running on port 5000...", file=sys.stderr, flush=True)
        app.run(host="0.0.0.0", port=5000, debug=True)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr, flush=True)
    import traceback
    traceback.print_exc()
