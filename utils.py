import tinydb
from tinydb import TinyDB
from tinydb_appengine.storages import EphemeralJSONStorage

def get_url(topic):
    try:
        db = tinydb.TinyDB('./gist_db.json', storage=EphemeralJSONStorage)
    except Exception as e:
        print(e)
    query = tinydb.Query()
    result = db.get(query.name == topic)['url']
    print(result)
    return result

