from flask import Flask, render_template, request
from deta import Deta
import requests
import utils
import os

deta = Deta("a047pg0i_9AWgmcVXv8x1JJBM6iQZkMj6gTsm1Q1g")
# deta = Deta(os.getenv('DB_PASS'))

db = deta.Base("cheatsheets")
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<topic>")
def hints(topic):
    try:

        url = db.get(topic)["url"]
        payload = requests.get(url).text

        if "|" in payload:
            piped_payload = utils.piped_parser(payload)
            return piped_payload

        else:
            return payload

    except:
        return "No hints found!"


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        topic = request.form["topic"]
        url = request.form["url"]
        is_gist = utils.check_is_gist(url)

        if is_gist:
            db.put({"key": topic, "url": url})
            return render_template("success.html")

        else:
            print("Error")
            return render_template(
                "error.html", error="The url you entered is not a valid gist url."
            )

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
