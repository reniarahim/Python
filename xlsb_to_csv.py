import os
import pandas as pd
import csv
from pyxlsb import open_workbook
import fnmatch


def convert_xlsb_to_csv(xlsb_file_name):
    print('Converting File : ' + xlsb_file_name)
    wb1 = open_workbook(xlsb_file_name)
    sheet1 = wb1.get_sheet(1)
    df = []

    for row in sheet1.rows(sparse=True):
        df.append([item.v for item in row])

    df = pd.DataFrame(df[1:], columns=df[0])
    csv_file_name = xlsb_file_name.replace('xlsb', 'csv')
    print(csv_file_name)
    df.to_csv(csv_file_name, index=False)
    wb1.close()


file_name = 'input*.xlsb'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, file_name):
        convert_xlsb_to_csv(file)
print("File Conversion Completed Successfully..")
