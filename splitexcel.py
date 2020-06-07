# import pandas as pd
# import os
# from openpyxl import load_workbook
# import xlswriter
# from shutil import copyfile
#
# file = input('File Path: ')
# extension = os.path.splitext(file)[1]
# filename = os.path.splitext(file)[0]
# pth = os.path.dirname(file)
# newfile = os.path.join(pth, filename + ' 2' + extension)
# df = pd.read_excel (file)
# colpick = input('Select Column: ')
# cols = list(set(df[colpick].values))
#
# def send_to_file(cols):
#     for i in cols:
#         df[df[colpick]==i].to_excel("{}/{}.xlsx".format(pth, i), sheet_name = i, index = False)
#         print('\nCompleted')
#         print('Thanks for using this program')
#         return
#
# def send_to_sheet(cols):
#     copyfile(file, newfile)
#     for j in cols:
#         writer = pd.ExcelWriter(newfile, engine='openpyxl')
#         for myname in cols:
#             mydf = df.loc[df[colpick] == myname]
#             mydf.to_excel(writer, sheet_name = myname, index = False)
#         writer.save()
#     print('\nCompleted')
#     print('Thanks for using this program.')
#     return
#
# print('Your data will be split based on these values {} and create {} files or sheets based on next selection. If you are ready to procede, please type "Y" and hit ENTER.  Type "N" to exit.'.format(', '.join(cols), len(cols)))
# while True:
#     x= input('Ready to proceed (Y/N): ').lower()
#     if x == 'y':
#         while True:
#             s = input('Split into different sheets or File (S/F): ').lower()
#             if s == 'f':
#                 send_to_file(col)
#                 break
#             elif s == 's':
#                 send_to_sheet(col)
#                 break
#             else:
#                 continue
#         break
#     elif x == 'n':
#         print('\nThanks for using this program.')
#         break

x = '\u1F4A9'
print(x)


