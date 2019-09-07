"""
注意到consumer函数是一个generator，把一个consumer传入produce后：
首先调用c.send(None)启动生成器；
然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
consumer通过yield拿到消息，处理，又通过yield把结果传回；
produce拿到consumer处理的结果，继续生产下一条消息；
produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
最后套用Donald Knuth的一句话总结协程的特点：
“子程序就是协程的一种特例。”
"""


# def consumer():
#     while 1:
#         data = yield n
#         print("消费者消费了第{}个包子".format(str(data)))
#
#         n = data
#
# def produce():
#     c.__next__() # 启动生成器 相当于 c.send(None)
#     i = 1
#     import time
#     while 1:
#         time.sleep(1)
#         print("生产者生产了第{}个包子".format(str(i)))
#         n = c.send(i)
#         print("消费者对第{}个包子付了钱".format(str(n)))
#         i+=1
#
#
# if __name__ == '__main__':
#     c = consumer()
#     produce()



def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)