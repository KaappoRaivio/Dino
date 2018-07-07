
from threading import Thread
import time, requests

ID = "id"

class ServerHandler(Thread):
    def __init__(self, url="http://localhost:5000/"):
        super().__init__()

        self.url = url



    def openConnection(self):
        r = requests.get(self.url + "open-connection/")
        self.conn_ID = int(r.text)

    def refreshConnection(self):
        payload = {ID: self.conn_ID}
        return requests.post(self.url + "refresh-connection/", payload)


a = ServerHandler()
a.openConnection()

print("waiting")
time.sleep(1)

print(a.refreshConnection())