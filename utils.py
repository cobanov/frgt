import tinydb

def get_url(topic):
    db = tinydb.TinyDB('gist_db.json')
    query = tinydb.Query()
    result = db.get(query.name == topic)['url']
    return result

