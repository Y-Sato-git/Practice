#2020/05/23
#リモートリポジトリ再作成

#標準入力
a = input("文字を入力してください : ")
b = int(input("数字を入力してください :"))

#繰り返し
for i in range(b):
    print(a,end="")
print()

#2020/05/24
#timeモジュール
#breakとcontinue

import time
while True:
    intTime = int(input("カウントダウンします。秒数を指定してください　：　"))
    if intTime <= 0:
        print("自然数を入力してください")
        continue
    else:
        break

while intTime >= 1:
    print(intTime,end=",")
    intTime -= 1
    time.sleep(1)
    if intTime == 0:
        print("タイムアップ！")
