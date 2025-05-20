nenrei: int = 1

if nenrei < 20:
    print('未成年です。')
    print('地方自治体によっては医療費が￥200のところも')
elif nenrei < 60:
    print('成年です。')
    print('飲酒・喫煙は控えめに。')
elif nenrei <= 100:
    print('定年後も元気100％で過ごしてください。')
