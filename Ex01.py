# (1)変数aに3、変数bに4を代入
a = 3
b = 4

# (2)a×bの結果表示
print(a*b)

# (3)'3×4=12'を変数を使って表示
print(str(a)+'×'+str(b)+'＝'+str(a*b))

# (4)文字列から数字部分を取り出し
c = 'value: '
d = '12345'
bun = c+d
bun = bun[7:]
print(bun)

# (5)文字列の置き換え "dog　→　cat"
like = 'I like dog.'
like = like.replace('dog', 'cat')

print(like)
