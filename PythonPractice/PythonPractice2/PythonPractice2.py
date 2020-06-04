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

if flg == ("20200602" or "ALL"):

#2020/06/02
#defaultdict
    from collections import defaultdict

    strLine = input("文字列を入力してください　：　")

    #0で初期化
    d = defaultdict(int)

    for c in strLine:
        d[c] += 1
    print(d)

if flg == ("20200603" or "ALL"):

#2020/06/03
#Class
    inName = input("Name : ")
    inAge = int(input("Age  : "))

    class Person(object):
        def name(self,strName):
            print(strName,"さん")
        def age(self,intAge):
            print(str(intAge),"歳")

    person = Person()
    person.name(inName)
    person.age(inAge)

if flg == ("20200604" or "ALL"):

#2020/06/04
#ファイル(プロジェクトと同じフォルダに格納される)

    #書き込み
    f = open('test.txt','w')
    f.write('test')
    f.close()

    #読み込み
    f = open('test.txt','r')
    #3文字目(0から始まるので）
    f.seek(2)
    print(f.read(1))
    '''
    以下のようにwithステートメントを使うと、自動でcloseしてくれる。
    with open('test.txt','w') as f:
        f.write('test')
    '''
