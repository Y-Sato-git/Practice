#2020年6月分
flg =  input("YYYYMMDDの日付 または ALL ⇒ ")
print(flg)

if flg == ("20200601" or "ALL"):

#2020/06/01
#例外処理
    l = [1,2,3,4,5]
    
    try:
        intNum = int(input("数字を入力してください　：　"))
        print(l[intNum + 1])
    except IndexError as ex:
        print("リストにありません。エラー内容⇒{}".format(ex))
    except Exception as ex:
        print("エラー内容⇒{}".format(ex))
