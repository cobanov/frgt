
def check_is_gist(url):
    """
    Checks if the url is a gist
    :return: True if the url is a gist, False if it is not
    """
    return url.startswith('https://gist.githubusercontent.com/')