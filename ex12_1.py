import os
import shutil

os.mkdir('date')
with open('tmp.txt', 'w') as f:
    print('', file=f)
shutil.move('tmp.txt','date')