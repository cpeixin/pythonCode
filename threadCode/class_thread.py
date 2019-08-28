# coding:utf-8
import threading


class Data:
    def __init__(self, data=None):
        self.data = data

    def get(self):
        return self.data

    def set(self, data):
        self.data = data


def test(name, data):
    print("in thread {} name is {}".format(threading.current_thread(), name))
    print("data is {} id(data) is {}".format(data.get(), id(data)))


if __name__ == '__main__':
    d = Data(10)
    name = "cpeixin"
    print("in main thread id(data) is {}".format(id(d)))
    for i in range(5):
        th = threading.Thread(target=test, args=(name, d))
        th.start()
