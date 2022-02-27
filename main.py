from flask import Flask, render_template, request
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
        url = utils.get_url(topic)[0]
        payload = requests.get(url).text

        # if name and url are separated by a pipe, split them
        try:
            piped_payload = ""
            piped = payload.split('\n')
            max_length = max([len(line) for line in piped])
            for line in piped:
                name, url = line.split('|')
                piped_payload += f"{name : <{int(max_length/2)}}{url}\n"
            return piped_payload
        except:
            return payload

    except Exception as e:
        print(e)
        pass
    
    return "No hints found."


@app.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        topic = request.form['topic']
        url = request.form['url']
        is_gist = utils.is_gist(url)

        if is_gist:
            utils.add_topic(topic, url)
            render_template("success.html")

        else:
            print('Error')
            render_template('error.html', error="The url you entered is not a valid gist url.")
    
    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True)