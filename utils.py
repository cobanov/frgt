def check_is_gist(url):
    """
    Checks if the url is a gist
    :return: True if the url is a gist, False if it is not
    """
    return url.startswith("https://gist.githubusercontent.com/")


def piped_parser(payload):
    """
    :param payload: The payload to be parsed
    :return: A string of text.
    """
    piped_payload = "\n🔥 Cool it is Piped Parsing!\n\n"
    piped = payload.split("\n")
    max_length = max([len(line) for line in piped])
    for line in piped:
        command, *desc = line.split("|")
        if not desc:
            desc = ""
        print(command, desc)
        piped_payload += f"{command : <{int(max_length/2)}}\t{desc}\n"
    return piped_payload
