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
# #     r = '' # 3
# #     while True:
# #         n = yield r # step4  # step8 （r赋值'200k'）
# #         if not n: # step7 （n=1）
# #             return
# #         print('[CONSUMER] Consuming %s...' % n)
# #         r = '200 OK'
# #
# # def produce(c):
# #     c.send(None) # 2 # 5
# #     n = 0
# #     while n < 5:
# #         n = n + 1
# #         print('[PRODUCER] Producing %s...' % n)
# #         r = c.send(n) # step6 (将send(1)中的1强制赋给 yield 左边的变量)  # step9 （r接收到yield返回右边变量的值，r=200k）
# #         print('[PRODUCER] Consumer return: %s' % r) # step10
# #     c.close()
# #
# # c = consumer()
# # produce(c) # step1



import inspect

def generator():
     i = '激活生成器' # 4
     while True:
        try: #8
            value = yield i # 5 , # 9 value =  Hello Shiyanlou ,返回 i的值给第10步
        except ValueError:
             print('OVER')
        i = value # 7 i=value=Hello Shiyanlou


g = generator()  # 1
inspect.getgeneratorstate(g)  # 2
print(next(g)) # 3 # 5
inspect.getgeneratorstate(g)
print(g.send('Hello Shiyanlou')) #6 # 10
g.throw(ValueError)

g.close()

inspect.getgeneratorstate(g)
