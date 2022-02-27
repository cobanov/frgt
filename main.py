from flask import Flask, render_template
import requests
import utils

app = Flask(__name__)

@app.route("/")
def index():
    """
    It renders the index.html template
    :return: The rendered template of the index.html file.
    """
    return render_template("index.html")

@app.route('/<topic>')
def hints(topic):
    """
    The function takes a topic as an argument, and returns the hints for that topic
    
    :param topic: The topic you want hints for
    :return: A string.
    """
    try:
        url = utils.get_url(topic)
        payload = requests.get(url).text
        return payload

    except Exception as e:
        print(e)
        pass
    
    return "No hints found."

@app.route('/add')
def add():
    return render_template("add.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)