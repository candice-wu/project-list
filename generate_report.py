#!/usr/bin/env python3

# The goal of the script is to read the CSV file and generate a report with the total number of people in each department.
# To achieve this, we will divide the script into three functions.
# First function: read_employees()



# [Step1] Convert employee data to dictionary
# read_employees()函式接收CSV檔案作為參數，並讀取該文件內容且轉成字典列表型態

import csv

def read_employees(csv_file_location):
# 定義read_employees()函式，並將file_location（employees.csv的路徑）作為參數

  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  #註冊一個dialect "empDialect"物件，並讓dialect當作參數傳遞給此read_employees()函式

  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  # 利用csv模組的DictReader()去讀取指定的csv檔案內容並轉成Dictionary資料型態以創建一個employee_file物件
  # 另外有一個dialect "empDialect"物件當作參數，最大目的是在解析指定的CSV檔案且同時也移除leading spaces

  employee_list = []
  # 建立一個空串列並指派給employee_list變數

  for data in employee_file:
    employee_list.append(data)
  # 以For Loops逐一讀取employee_file物件的內容，再將值寫進employee_list串列變數

  return employee_list
  # 回傳employee_list結果值

employee_list = read_employees('/Users/candicewu/git_project/employees.csv')
# 呼叫read_employees()函式並將結果儲存至employee_list串列變數
# read_employees()函式的參數值＝指定被解析的CSV檔案的完整路徑

print(employee_list)
# 印出employee_list串列變數以檢查它是否返回字典列表




# [Step2] Process employee data
# process_data()函式接收employee_list串列變數作為參數，並計算一個部門有多少員工，再以字典型態寫進指定變數

def process_data(employee_list):
# 定義process_data()函式，並將employee_list串列變數作為參數

  department_list = []
  # 建立一個空串列並指派給department_list變數

  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  # 以For Loops逐一讀取employee_list串列變數的內容（限定Department），再將值寫進department_list串列變數

  department_data = {}
  # 建立一個空字典並指派給department_data變數

  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data
  # 以For Loops逐一讀取department_list串列變數的內容且以count()得出該串列變數裡的部門名稱的小計（即各部門的員工數量）
  # 再將結果-部門名稱：小計（department[key]=value為字典的指派寫法）寫進department_data字典變數

dictionary = process_data(employee_list)
# 呼叫process_data()函式並將結果儲存至dictionary字典變數
# process_data()函式的參數值＝employee_list串列變數

print(dictionary)
# 印出dictionary字典變數




# [Step3] Generate a report
# 生成報表

def write_report(dictionary, report_file):
# 定義write_report()函式，並將dictionary字典變數、report_file（指定的儲存路徑）作為參數

    with open(report_file, "w+") as f:
    # 以w+模式開啟指定檔案（該文件若已存在則會直接開啟執行w+指令；否則會先自動生成再執行w+指令
    # w+模式：開啟執行讀取和寫入行為，且會覆蓋原文件內容
    # 並取別名為f

        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        # 以For Loops逐一讀取dictionary字典變數，並依指定格式（部門名稱：員工數量）寫入該文件（f）

        # f.close()
        # 關閉文件

write_report(dictionary, '/Users/candicewu/git_project/report.txt')
# 利用dictionary字典變數、report_file（指定的儲存路徑）去呼叫write_report函式，並在指定的儲存路徑生成report.txt
