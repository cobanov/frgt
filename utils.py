import psycopg2

conn = psycopg2.connect(
        database="d2pqfemoj0ksmj", 
        user='hocbijyicddzcd', 
        password='4e5491e5f4b441c81f229e6f554c0ca047059326b5750421ae536d81ea89f0f8', 
        host='ec2-34-233-157-9.compute-1.amazonaws.com', 
        port= '5432'
    )

def fetch_all():
    """
    Fetches all the topics from the database
    :return: A list of all the topics
    """

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    query = """
            SELECT * FROM cheatsheets"""
    cursor.execute(query)

    # Commit your changes in the database
    data = cursor.fetchall()

    # Closing the connection
    conn.close()
    return data

def get_url(topic):
    """
    Gets the url of the topic
    :return: The url of the topic
    """

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    query = """
            SELECT url FROM cheatsheets WHERE topic = '{}'""".format(topic)
    cursor.execute(query)

    # Commit your changes in the database
    url = cursor.fetchone()

    # Closing the connection
    conn.close()
    return url

def add_topic(topic, url):
    """
    Adds a topic to the database
    :param topic: The topic you want to add
    :param url: The url you want to add
    :return: None
    """

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    query = """
            INSERT INTO cheatsheets(topic, url) VALUES ('{}', '{}')""".format(topic, url)
    cursor.execute(query)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()
    
def check_is_gist(url):
    """
    Checks if the url is a gist
    :return: True if the url is a gist, False if it is not
    """
    return url.startswith('https://gist.githubusercontent.com/')