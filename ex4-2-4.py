students_data = [{'name': 'A', 'math': 85, 'english': 92, 'science': 78},
                 {'name': 'B', 'math': 70, 'english': 81, 'science': 88},
                 {'name': 'C', 'math': 95, 'english': 88, 'science': 92},
                 {'name': 'D', 'math': 60, 'english': 75, 'science': 70},
                 {'name': 'E', 'math': 88, 'english': 90, 'science': 85}]
# ① mathの平均点
ave = 0
# for i in range(len(students_data)):
#     ave += students_data[i].get('math')
for i in students_data:
    ave += i['math']
ave = ave / len(students_data)
print('数学の平均点：'+str(ave)+'点')

# ② scienceの点数が最も高い生徒の名前とその点数
max_score = 0
top = ''
for i in students_data:
    if i['science'] > max_score:
        max_score = i['science']
        top = i

print(top['name'], str(max_score)+'点')

# ③ 教科合計点を計算し各学生の辞書にtotalというキーで合計点を追加
SAM = 0
for i in students_data:
    SAM = i['math']+i['english']+i['science']
    i['total'] = SAM

print(students_data)
