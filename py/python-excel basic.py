from openpyxl import load_workbook
from openpyxl.drawing.image import Image

wb = load_workbook('a.xlsx')
ws1 = wb.active
img = Image(r'E:\BaiduNetdiskDownload\纪龙山合集\微信图片_20201022151922.jpg')
ws1.add_image(img, 'A1')

# 保存文件
wb.save("a.xlsx")
