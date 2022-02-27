from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tmux")
def tmux():
    URL = 'https://gist.githubusercontent.com/cobanov/e0a8f27f492149fd949cb82cbd05bf33/raw/0b8ec61e182d0a184cb2c841197952df6abce494/tmux.txt'
    r = requests.get(URL)

    return r.text

@app.route("/vim")
def vim():
    URL = 'https://gist.githubusercontent.com/cobanov/65aed70d56f4fe832c6c62614ce47650/raw/fdcbd9d9af342ce6a3a07ffed2774de737de93bb/vim.txt'
    r = requests.get(URL)

    return r.text

@app.route("/repo")
def repo():
    URL = 'https://gist.githubusercontent.com/cobanov/73f5b8dfd07d302004ce7f43c85ccdd3/raw/d084e3f67fd6cb075e81cd3fd9216da582d00b01/repo.txt'
    r = requests.get(URL)

    return r.text
    
@app.route("/love")
def love():
    URL = 'https://gist.githubusercontent.com/cobanov/5bea979f7785fcfad8aa80db308212ab/raw/c59c4e3f52fc58f86fd4155dea16b4720f7893e3/love.txt'
    r = requests.get(URL)

    return r.text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)