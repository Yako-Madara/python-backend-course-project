from flask import Flask
from logic import get_feed_for_category

app = Flask(__name__)


@app.route("/<category>")
def feed_for_category(category: str):
    return get_feed_for_category(category)


if __name__ == "__main__":
    app.run()
