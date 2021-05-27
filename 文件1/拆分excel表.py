import pandas as pd
from datetime import datetime as dt

# file=pd.read_excel(r'C:\Users\Administrator\Desktop\file\test.xls',sheet_name="销售总表")
file = pd.read_excel(r"H:\muqia_data\链接\银行反馈数据\恒丰-宁波\恒丰数据-上分（完整）-2021.4.27.xlsx", sheet_name=u'核卡')
print(file.head())
menu = file.iloc[:, -1].drop_duplicates()
for name in menu:
    df1 = file[file.渠道 == name]
    print(len(df1))
    path = "H:\\wait_data\\" + name + "恒丰数据反馈4.27.xlsx"
    df1.to_excel(path, index=None)

