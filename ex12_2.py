import os
import os.path
import datetime


#
#
# def ListUp_old_files(path, n_days: int):
#     day = n_days
#     today = datetime.datetime.now()
#     if not os.path.exists(path):
#         print('パスが存在しません')
#     li = os.listdir(path)
#     for i in range(len(li)):
#         s = os.path.getmtime(li[i])
#         s1 = datetime.datetime.fromtimestamp(s)
#     if s1.day < today.day - day:
#         print(s1)
#     else:
#         print(f'{day}日前に更新されたファイルはありません')
#
#
# ListUp_old_files('C:/Users/Miura Ayaha/Desktop/', 10)
#

import os
import datetime


def ListUp_old_files(path, n_days: int):
    # 現在の日付と時刻を取得
    today = datetime.datetime.now()

    # 指定されたパスが存在しない場合
    if not os.path.exists(path):
        print('パスが存在しません')
        return  # パスが無ければここで終了

    # ディレクトリ内のファイル・ディレクトリをリストアップ
    li = os.listdir(path)
    found = False  # 更新されたファイルが見つかったかどうか

    # 指定された日数前の日付を計算
    time_limit = today - datetime.timedelta(days=n_days)

    for filename in li:
        # 各ファイル/ディレクトリのフルパスを作成
        file_path = os.path.join(path, filename)

        # ファイルかディレクトリかを確認し、更新日時を取得
        if os.path.exists(file_path):  # 存在するファイル・ディレクトリに対して
            try:
                mtime = os.path.getmtime(file_path)  # 最終更新日時を取得
                mtime_dt = datetime.datetime.fromtimestamp(mtime)  # タイムスタンプを日時に変換

                # 最終更新日時が指定された日数以内であれば
                if mtime_dt > time_limit:
                    print(f'{filename} は {mtime_dt} に更新されました')
                    found = True
            except Exception as e:
                print(f'{filename} に対してエラーが発生しました: {e}')

    if not found:
        print(f'{n_days}日前に更新されたファイルはありません')


# 実行例
ListUp_old_files('C:/Users/Miura Ayaha/Desktop/', 10)
