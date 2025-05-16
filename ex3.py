# (1)リスト定義
a = [10, 8, 12, 17, 5]

# (2)リストの末尾表示
print(a[-1])

# (3)リストの末尾に'13'追加
a.append(13)
# print(a)

# (4)リストbにリストaをソートした要素代入
b = sorted(a)
print(b)

# (5)キーと日本語訳を値とする辞書を定義
d = {'dog': '犬', 'cat': '猫', 'bird': '鳥'}

# (6)catの日本語訳表示
print(d['cat'])

# (7)辞書の中にmonkeyが含まれているか
print('monkey' in d)
