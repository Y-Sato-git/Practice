import tkinter as tk
from tkinter import filedialog
import openpyxl

def file_open():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws["A1"] = "TEST"
    wb.save(str(input_box) + '.xlsx')

#ウインドウの作成
root = tk.Tk()
root.title("FileSelect")
root.geometry("500x3000")

#入力欄の作成
input_box = tk.Entry(width=40)
input_box.place(x=10, y=100)

#ラベルの作成
input_label = tk.Label(text="結果")
input_label.place(x=10, y=70)

#ボタンの作成
button = tk.Button(text="作成",command=file_open)
button.place(x=10, y=130)
button2 = tk.Button(text="終了",command = root.destroy)
button2.place(x=150,y=130)

#ウインドウの描画
root.mainloop()

