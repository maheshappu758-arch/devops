from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>OCI Python App</title></head>
    <body style="font-family:Arial,sans-serif; text-align:center; margin-top:80px; background:#0a0f1c; color:#fff;">
        <h1 style="font-size:2.5rem;">🚀 Hello from Oracle Cloud!</h1>
        <p style="font-size:1.2rem; color:#aaa;">A simple Python Flask app running on OCI.</p>
        <a href="/health" style="color:#4f9cff;">Check Health Status</a>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "oci-python-app"}), 200

@app.route("/about")
def about():
    return jsonify({
        "app": "OCI Python App",
        "version": "1.0.0",
        "framework": "Flask",
        "cloud": "Oracle Cloud Infrastructure"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
