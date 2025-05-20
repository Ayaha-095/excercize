li = []
for i in range(1, 10):
    for j in range(1, 10):
        a = i*j
        if a % 2 == 0 and a % 3 == 0:
            # 6の倍数
            print('##',end='\t')
        elif a % 3 == 0:
            print('@@',end='\t')
        elif a % 2 == 0:
            print('**',end='\t')
        else:
            print(i*j, end='\t')
    print()





