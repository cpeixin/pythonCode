import json
import time
import random
import os
from multiprocessing import Process,Lock,Pool

def chakan():
    dic = json.load(open('piao',))  # 先查看票数，也就是打开那个文件
    print('剩余票数：%s' % dic['count'])  # 查看剩余的票数


def buy():
    dic = json.load(open('piao',))
    if dic['count']>0: #如果还有票
        dic['count']-=1 #就修改里面的值-1
        time.sleep(random.randint(1,3)) #执行里面买票的一系列操作就先不执行了，让睡一会代替（并且随机的睡）
        json.dump(dic,open('piao','w'))
        print('%s 购票成功' % os.getpid())  # 当前的那个id购票成功


def task(mutex): #抢票
    # mutex.acquire() #加锁
    # chakan()  # 因为查看的时候大家都可以看到，不需要加锁
    # buy() #买的时候必须一个一个的买，先等一个人买完了，后面的人在买
    # mutex.release() #取消锁

    with mutex:
        chakan()  # 因为查看的时候大家都可以看到，不需要加锁
        buy() #买的时候必须一个一个的买，先等一个人买完了，后面的人在买


if __name__ == '__main__':
    mutex = Lock()
    pool = Pool(20)

    """进程池加锁
    """
    from multiprocessing import Pool, Manager, Lock

    manager = Manager()
    mutex = manager.Lock()


    for i in range(50):#让50个人去访问那个票数
        pool.apply_async(task,args=(mutex, ))
    pool.close()
    pool.join()


# 这里实现的就是多个进程之间共享内存，并修改数据
# 这里不需要加锁，因为manager已经默认给你加锁了