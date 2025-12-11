import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"status": "ok", "msg": "Cloud Run funcionando"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
