"""
题目：LRU 缓存机制 设计和实现一个 LRU（最近最少使用）缓存数据结构，使它应该支持一下操作：get 和 put。
get(key) - 如果 key 存在于缓存中，则获取 key 的 value（总是正数），否则返回 -1。
put(key,value) - 如果 key 不存在，请设置或插入 value。当缓存达到其容量时，它应该在插入新项目之前使最近最少使用的项目作废。

出题人：文景／阿里云 CDN 资深技术专家
"""

"""
应用场景： 在Android 2.2以上的sdk中提供了缓存类LruCache。LruCache用于内存缓存，常用的应用场景有很多，比如我们的图片加载库的内存缓存就可以利用LruCache来实现
"""


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.cache = {}
        self.keys = []
        self.capacity = capacity

    def visit_key(self, key):
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

    def elim_key(self):
        key = self.keys[0]
        self.keys = self.keys[1:]
        del self.cache[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.cache:
            return -1
        self.visit_key(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not key in self.cache:
            if len(self.keys) == self.capacity:
                self.elim_key()
        self.cache[key] = value
        self.visit_key(key)  ## 在put和get元素时，要先清除此元素，在追加，改变一下位置。


def main():
    s = [["put", "put", "get", "put", "get", "put", "get", "get", "get"], [[1, 1], [2, 2], [1], [3, 3], [2], [
        4, 4], [1], [3], [4]]]
    obj = LRUCache(2)
    l = []
    for i, c in enumerate(s[0]):
        if (c == "get"):
            l.append(obj.get(s[1][i][0]))
        else:
            obj.put(s[1][i][0], s[1][i][1])
    print(l)


if __name__ == "__main__":
    main()