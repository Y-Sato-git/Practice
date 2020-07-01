ymd = input("年月日をYYYYMMDD入力　：　")

#例外
if ymd == "20200701":
    import traceback
    n = int(input("整数を入力してください　：　"))

    try:
        ans = 100 / n
        print(ans)
    except ZeroDivisionError as e:
        print(traceback.format_exc())