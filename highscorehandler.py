
from threading import Thread
import time, requests, sys

sys.path.append("/home/kaappo/git/dinoserver/")

import constants

class ServerHandler(Thread):
    def __init__(self, url="http://localhost:5000/"):
        super().__init__()

        self.url = url
        self.start()

    @staticmethod
    def getCurrentHighscore():
        return requests.get(self.url + "get-highscore/").text

    def openConnection(self):
        r = requests.post(self.url + "open-connection/", data={constants.NICKNAME: "Kaappo"})
        self.conn_ID = int(r.text)

    def refreshConnection(self):
        payload = {constants.ID: self.conn_ID}
        print(requests.post(self.url + "refresh-connection/", payload))

    def run(self):
        self.openConnection()
        while True:
            self.refreshConnection()
            time.sleep(1)

    def reportScore(self, score):
        payload = {constants.ID: self.conn_ID, constants.SCORE_KEY: score * self.conn_ID}
        return requests.post(self.url + "set-score/", data=payload)


a = ServerHandler()

print("sleeping")
time.sleep(5)
print("woke")

a.reportScore(10)
# time.sleep(1)

# print(a.refreshConnection())