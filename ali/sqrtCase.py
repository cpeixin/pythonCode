"""
题目：已知 sqrt (2)约等于 1.414，要求不用数学库，求 sqrt (2)精确到小数点后 10 位。
出题人：——阿里巴巴出题专家：文景／阿里云 CDN 资深技术专家
参考答案：
* 考察点
基础算法的灵活应用能力（二分法学过数据结构的同学都知道，但不一定往这个方向考虑；如果学过数值计算的同学，应该还要能想到牛顿迭代法并解释清楚）
退出条件设计
"""

EPSINON = 0.0000000001

low = 1.4
high = 1.5

mid = (high + low) / 2

while (high - low) > EPSINON:
    if (mid * mid) > 2:
        high = mid
    else:
        low = mid
    mid = (high + low) / 2
print(mid)# 1.4142135623376817
print(1.4142135623376817*1.4142135623376817)#1.999999999899836