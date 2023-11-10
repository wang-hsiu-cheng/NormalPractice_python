import numpy as np
import matplotlib.pyplot as plt
import xlrd

#範例檔：free fall data.xlsx

myWorkbook = xlrd.open_workbook('free fall data.xlsx')             #獲取excel工作簿
pingpong_data = myWorkbook.sheet_by_index(0)            #讀第1個分頁
styrofoam_data = myWorkbook.sheet_by_index(1)           #讀第2個分頁

pingpong_data_rows = pingpong_data.nrows                #pingpong數據列數
pingpong_data_columns = pingpong_data.ncols             #pingpong數據行數
print(pingpong_data_rows, pingpong_data_columns)

pingpong_t = np.array([pingpong_data.cell(i,0).value for i in range(1,pingpong_data_rows)])
pingpong_y = np.array([pingpong_data.cell(i,1).value for i in range(1,pingpong_data_rows)])
print(pingpong_t, pingpong_y)

plt.figure(figsize=(8,6))
plt.scatter(pingpong_t,pingpong_y,color="red",label="Sample Point",linewidth=3)

plt.legend()
plt.show()
