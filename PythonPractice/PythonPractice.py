flg = input("YYYYMMDDの日付 または ALL ⇒ ")
print(flg)

if flg == ("20200523" or "ALL"):

#2020/05/23
#リモートリポジトリ再作成
#標準入力
    print()
    a = input("文字を入力してください : ")
    b = int(input("数字を入力してください :"))

#繰り返し
    for i in range(b):
	    print(a,end="")
    print()

if flg == ("20200524" or "ALL"):

#2020/05/24
#timeモジュール
#breakとcontinue
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

if flg == ("20200525" or "ALL"):

#2020/05/25
#Happy Birthday
#math
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

if flg == ("20200526" or "ALL"):
#2020/05/26
#スライス
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

if flg == ("20200527" or "ALL"):
#2020/05/27
#.joinなど
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

if flg == ("20200528" or "ALL"):
#2020/05/28
#flgにALL追加
#余白
    print()
    intNum = int(input("数値を入力してください。　：　"))
    print("'{:<10}'.format(intNum)  ⇒ " , '{:<10}'.format(intNum))
    print("'{:>10}'.format(intNum)  ⇒ " , '{:>10}'.format(intNum))
    print("'{:^10}'.format(intNum)  ⇒ " , '{:^10}'.format(intNum))
    print("'{:=10}'.format(intNum)  ⇒ " , '{:=10}'.format(intNum))
    print("'{:*<10}'.format(intNum) ⇒ " , '{:*<10}'.format(intNum))
    print("'{:*>10}'.format(intNum) ⇒ " , '{:*>10}'.format(intNum))
    print("'{:*^10}'.format(intNum) ⇒ " , '{:*^10}'.format(intNum))
    print("'{:*=10}'.format(intNum) ⇒ " , '{:*=10}'.format(intNum))

if flg == ("20200529" or "ALL"):
#2020/05/29
#sort(失敗。原因不明。)
    intNum2 = input("数字をカンマ区切りで入力してください。　：　").split(',')

    sortA = sorted(intNum2)
    sortB = sorted(intNum2, reverse=True)

    print("入力　　　　　　　：　" , str(intNum2))
    print("並び替え（昇順）　：　" , str(sortA))
    print("並び替え（降順）　：　" , str(sortB))

if flg == ("20200530" or "ALL"):
#2020/05/30
#def(関数の作り方)
    print("関数の作り方 : def + 関数名(仮引数)")

    #関数部分
    def ast(n):
        for _ in range(n):
            print("*",end = '')

    #関数呼び出し
    i = int(input("自然数を入力してください　：　"))
    ast(i)
    print()