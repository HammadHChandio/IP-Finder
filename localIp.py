import socket


# Finding out local IP address
class LocalIp:
    def __init__(self):
        self.ip = None

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.ip = s.getsockname()[0]
        s.close()
        return self.ip
