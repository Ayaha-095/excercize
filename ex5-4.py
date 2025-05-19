import time


def active_time(func):
    def dif(*args, **kwargs):
        s = time.perf_counter()  # スタート
        result = func(*args, **kwargs)  # 元の関数の処理実行
        e = time.perf_counter()  # エンド
        # 処理時間計測
        r = e - s
        print(f"{r:.7f}秒")
        # 引数の関数処理結果戻し
        return result

    return dif


@active_time
def add(a):
    sum_ = 0
    for i in range(10000):
        sum_ = a + sum_
    return sum_


@active_time
def adder(a):
    for i in range(1000):
        cul = i ** a
    return cul


add(900000)
adder(10000)
