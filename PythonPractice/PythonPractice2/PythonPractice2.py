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

if flg == ("20200605" or "ALL"):

#2020/06/05
#Excel自動化

    import openpyxl
    import docx

    strFileName = input("ファイル名：　")

    #workbookを開く
    wb = openpyxl.Workbook()

    #sheetを追加
    wb.create_sheet()

    #sheetの名前（一覧）
    print(wb.get_sheet_names())

    #sheet指定
    sheet = wb['Sheet']

    #cell指定
    c = sheet['A1']

    #cellの値変更
    c.value = "aaa"

    #2枚目
    sheet = wb['Sheet1']
    c = sheet['A1']
    c.value = "bbb"

    #保存
    wb.save(strFileName + ".xlsx")

if flg == ("20200606" or "ALL"):

#2020/06/06
#Excel自動化続き,Word自動化

    import openpyxl
    from openpyxl.styles import Font

    wb = openpyxl.Workbook()
    sheet = wb.active
    _font = Font(name="明朝",sz=15,b=True)

    for i in range(1,100):
        cell = sheet.cell(row=i,column=1,value=i)
        cell.font = _font

    wb.save("20200606.xlsx")

    import docx
    from docx import Document

    document = Document()
    document.add_paragraph("AAAAAAAAAA")

    document.save("20200606.docx")

    import os
    print(os.listdir('.'))

if flg == ("20200607" or "20200608" or "ALL"):

#2020/06/07,08
#Tkinterお試し作成（別プロジェクト・消滅してた）
    print("今日は別プロジェクト")

if flg == ("20200609" or "ALL"):

#2020/06/09
#logging
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('DEBUG')

if flg == ("20200610" or "ALL"):

#2020/06/10
#openpyxl
    print("今日は別プロジェクト")

if flg == ("20200611" or "ALL"):
    
#2020/06/11
#pandas
    import pandas
    import numpy

    array9 = numpy.array([1,2,3,4,5,6,7,8,9])
    dataframe9 = pandas.DataFrame({
        '1' : array9,
        '2' : array9 * 2,
        '3' : array9 * 3,
        '4' : array9 * 4,
        '5' : array9 * 5,
        '6' : array9 * 6,
        '7' : array9 * 7,
        '8' : array9 * 8,
        '9' : array9 * 9})
    print(dataframe9)

if flg == ("20200612" or "ALL"):
    
#2020/06/12
#計算

    import scipy
    import numpy

    sample_data = numpy.array([1,2,3,4,5])
    print("sample_data = numpy.array([1,2,3,4,5])")
    print("sum  : " , str(scipy.sum(sample_data)))
    print("mean : " , str(scipy.mean(sample_data)))
    print("var(ddof=0) : " , str(scipy.var(sample_data,ddof=0)))
    print("var(ddof=1) : " , str(scipy.var(sample_data,ddof=1)))
    print("std(ddof=0) : " , str(scipy.std(sample_data,ddof=0)))
    print("amax : " , str(scipy.amax(sample_data)))
    print("amin : " , str(scipy.amin(sample_data)))
    print("median : " , str(scipy.median(sample_data)))