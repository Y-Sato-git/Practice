import openpyxl
import pandas
import glob

import_file_path = input("読み込むファイルをパスから入力　：　")
excel_sheet_name = input("シート名　：　")
output_path = input("アウトプットファイルのパス　：　")

dataframe_order = pandas.read_excel(import_file_path,sheet_name = excel_sheet_name)
company_name = dataframe_order['会社名'].unique()
'''
for i in company_name:
    print(i)
'''
for i in company_name:
    dataframe_order_company = dataframe_order[dataframe_order['会社名'] == i]
    dataframe_order_company.to_excel(output_path + '\\' + i + '.xlsx')
    workbook = openpyxl.load_workbook(output_path + '\\' + i + '.xlsx')
    worksheet = workbook.worksheets[0]
    worksheet.delete_cols(1)
    workbook.save(output_path + '\\' + i + '.xlsx')