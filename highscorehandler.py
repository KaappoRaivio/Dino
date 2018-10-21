
from threading import Thread
import time, requests, sys

sys.path.append("/home/kaappo/git/dinoserver/")

import constants

class ServerHandler(Thread):
    _STOP = False

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
        while not self._STOP:
            self.refreshConnection()
            time.sleep(1)

        print("moi")

    def reportScore(self, score):
        payload = {constants.ID: self.conn_ID, constants.SCORE_KEY: score * self.conn_ID}
        return requests.post(self.url + "set-score/", data=payload)

    def __del__(self):
        self.stop()
        del self

    @classmethod
    def stopAllThreads(cls):
        cls._STOP = True
