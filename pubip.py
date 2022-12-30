import requests


# Finding out Public IP address
class PubIp:
    def __init__(self):
        self.ip = None

    def get_ip(self):
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            self.ip = response.text
        else:
            self.ip = "Error getting IP address"
