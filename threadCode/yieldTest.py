# encoding:UTF-8
def yield_test(n):
    for i in range(n): # step2 （i= 0） # step10
        yield call(i) # step3  # step5  # step11   # step13
        print("i=", i) # step9
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2 # step4  # step12


# 使用for循环
for i in yield_test(5): #step1  #step6  # step8   # step14 .........
    print(i, ",") # step7