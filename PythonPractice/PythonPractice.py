flg = input("YYYYMMDDの日付 : ")

if flg == "20200523":

#2020/05/23
#リモートリポジトリ再作成
#標準入力
    a = input("文字を入力してください : ")
    b = int(input("数字を入力してください :"))

#繰り返し
    for i in range(b):
	    print(a,end="")
    print()

elif flg == "20200524":

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

elif flg == "20200525":

#2020/05/25
#Happy Birthday
#math
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

elif flg == "20200526":
#2020/05/26
#スライス

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

elif flg == "20200527":
#2020/05/27
#.joinなど
    strB = input("文字列(strB) を入力してください：")
    print()
    print("''.join(strB)    : ",''.join(strB))
    print("' '.join(strB)   : ",' '.join(strB))
    print("','.join(strB)   : ",','.join(strB))
    print("' * '.join(strB) : ",' * '.join(strB))
    print("strB.capitalize():",strB.capitalize()) #最初の文字を大文字にする
    print("strB.upper()     :",strB.upper())      #すべての文字を大文字にする
    print("strB.center(20)  :",strB.center(20))   #中央ぞろえ
    print("strB.ljust(20)   :",strB.ljust(20))    #左ぞろえ
    print("strB.rjust(20)   :",strB.rjust(20))    #右ぞろえ

