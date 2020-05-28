flg = input("YYYYMMDDの日付 または ALL ⇒ ")

if flg == "20200523" or "ALL":

#2020/05/23
#リモートリポジトリ再作成
#標準入力
    print("\n20200523")
    print()
    a = input("文字を入力してください : ")
    b = int(input("数字を入力してください :"))

#繰り返し
    for i in range(b):
	    print(a,end="")
    print()

if flg == "20200524" or "ALL":

#2020/05/24
#timeモジュール
#breakとcontinue
    print("\n20200524")
    print()
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

if flg == "20200525" or "ALL":

#2020/05/25
#Happy Birthday
#math
    print("\n20200525")
    print()
    strName = input("Name : ")
    intAge = int(input("Age  : "))

    if strName != "" and intAge != "":
        print("*--------------------------------*")
        print(strName + "、" + str(intAge) + "歳のお誕生日おめでとう！")
        print("    良い一年になりますように！   ")
        print("*--------------------------------*")
        print()

    import math
    print(str(intAge) + "の平方根は" + str(math.sqrt(intAge)) + "です。")

if flg == "20200526" or "ALL":
#2020/05/26
#スライス
    print("\n20200526")
    print()
    strA = "ABCDEFGHIJ"
    #すべて
    print(strA[:])
    #先頭から5文字
    print(strA[0:5])
    #２文字おき
    print(strA[::3])
    #逆向き
    print(strA[::-1])
    #５文字目から最後まで
    print(strA[4:])
    #最後の５文字
    print(strA[-5:])

if flg == "20200527" or "ALL":
#2020/05/27
#.joinなど
    print("\n20200527")
    print()
    strB = input("文字列(strB) を入力してください：")
    print()
    print("''.join(strB)    : ",''.join(strB))
    print("' '.join(strB)   : ",' '.join(strB))
    print("','.join(strB)   : ",','.join(strB))
    print("' * '.join(strB) : ",' * '.join(strB))
    print("strB.capitalize():",strB.capitalize()) #最初の文字を大文字にする
    print("strB.upper()     :",strB.upper())      #すべての文字を大文字にする
    print()
    print("strB.center(20)      :",strB.center(20))       #中央ぞろえ
    print("strB.center(20,'*')  :",strB.center(20,'*'))   #中央ぞろえ(*で埋める。"*"にしたらエラーした。）
    print("strB.ljust(20)       :",strB.ljust(20))        #左ぞろえ
    print("strB.rjust(20)       :",strB.rjust(20))        #右ぞろえ

if flg == "20200528" or "ALL":
#2020/05/28
#flgにALL追加
    print("\n20200528")
    print()

