# coding:utf-8
import threading


def test(name, data):
    print("in thread {} name is {}".format(threading.current_thread(), name))
    print("data is {} id(data) is {}".format(data, id(data)))


if __name__ == '__main__':
    d = 'cpeixin'
    name = "cpeixin"
    for i in range(5):
        th = threading.Thread(target=test, args=(name, d))
        th.start()