import requests
from flask import Flask, request, Response

app = Flask(__name__)

# TEMPORAL: Para validar la IP pública del NAT
TARGET_URL = "https://ifconfig.me"

@app.route("/", methods=["GET", "POST"])
def proxy():
    resp = requests.request(
        method=request.method,
        url=TARGET_URL,
        headers={k: v for k, v in request.headers if k.lower() != "host"},
        params=request.args,
        data=request.get_data()
    )

    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers)
