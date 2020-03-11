def h():
    print('接下来 我要打印yield的接收值 m : ')
    m = yield 5  # Fighting! # step2
    print("m : "+m) # step4
    d = yield 12 # step5
    print('We are together!')

c = h()
m = c.__next__()  # step1 （yield 将右边的值返回，并赋予m ）
d = c.send('Fighting!') # step3 （将Fighting值发送给生成器，并强制赋给 step2 的m变量）# 6 (d接收 step5 yield返回右边的12)
print('We will never forget the date', m, '.', d)