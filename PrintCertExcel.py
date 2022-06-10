import pandas as pd
from inputExcel import getDatafromExcel

file = 'student.xlsx'
df = pd.read_excel(file)
gd = getDatafromExcel()
gd.getRow(df)
