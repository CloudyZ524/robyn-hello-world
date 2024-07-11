from robyn import Robyn
import os

app = Robyn(__file__)


@app.get("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    # Read the PORT environment variable for deployment
    port = int(os.getenv("PORT", 8080))
    app.start(host="0.0.0.0", port=port)
