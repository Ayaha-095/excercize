# (1)
prob = 0
money = 6000

if prob >= 80:
    print('天気が悪いので今日は家で過ごしましょう')
elif prob >= 40 and money >= 5000:
    print('雨が降りそうなので今日は映画を見に行きましょう')

elif prob < 40 and money >= 5000:
    print('天気がいいので今日は遠出しましょう')

elif prob < 40 and money < 5000:
    print('今日は近場で遊びましょう')

# (2)
SAM = 0
n = 1
while n <= 100:
    SAM += n
    n += 2
print(SAM)

# (3)
s = 0
for i in range(1, 100, 2):
    s += i
print(s)

# (4)
[i for i in range(1, 11) if i % 2 == 0]
