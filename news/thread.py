import threading
import time

class Thread(threading.Thread):
    def run(self):
        print("{} inicio".format(self.getName()))
        time.sleep(1)
        print("{} terminado".format(self.getName()))

if __name__ == "__main__":
    for i in range(4):
        thread = Thread(name="Thread {}".format(i+1))
        thread.start()
        time.sleep(.5)