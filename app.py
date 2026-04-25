from dotenv import load_dotenv
import os
from flask import Flask

load_dotenv()


app=Flask(__name__)


news_api_key = os.getenv("API_KEY")


@app.route("/")
def home():
    return f"My key is being loaded safely!"

if __name__ == "__main__":
    app.run(debug=True)