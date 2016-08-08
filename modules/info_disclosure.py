import requests


class Info_disclosure:
    """
    """
    def __init__(self):
        pass

    def robots(self, target):
        req = requests.get(target+"/robots.txt")
        r = req.text
        print(r)
