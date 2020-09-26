#Author Atticus_lv
#-*- coding =utf-8 -*-
#@Time : 2020/9/19 12:18

import time



seq = ['one', 'two', 'three']

def test1():
    start1 = time.perf_counter()
    i = 0
    for element in seq:
        print(i, seq[i])
        i += 1
    end1 = time.perf_counter()

    print("final is in : %s Seconds " % (end1-start1))


def test2():
    start1 = time.perf_counter()
    for i, element in enumerate(seq):
        print(i, element)

    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))

# test1()
time1 = 2.920000000000006e-05
# test2()
time2 = 2.8099999999999653e-05
