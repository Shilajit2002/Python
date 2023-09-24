import xlrd
import pandas as pd

loc = ("E:\\Python\\Code\\Tutorial\\Read Excel Data\\ExcelData.xls")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

print(sheet)

# print(pd.read_excel("E:\\Python\\Code\\Tutorial\\Read Excel Data\\ExcelData.xls"))