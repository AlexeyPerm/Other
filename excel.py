import xlrd
import subprocess
import telnetlib

# from tabulate import tabulate
# from pprint import pprint

rb = xlrd.open_workbook('text.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
head = vals[0]
vals.pop(0)
# result = []
ip = vals[2][4]


def tracert(ip_address = '178.161.240.2'):
    print('Выполняется трассировка... ')
    traceroute = subprocess.run(['traceroute','-f', '3', '-m', '4', '-q', '2', ip_address], stdout=subprocess.DEVNULL)
    return traceroute

print(tracert(ip))







# result = {}
# for line in vals:
#     result[line[0]] = line[4].split()

# 'traceroute','-f', '3', '-m', '4', '-q', '2'   (-f с третьего хопа, -m до 4 хопа, -q кол-во проб)
subprocess.run(['traceroute','-f', '3', '-m', '4', '-q', '2', vals[1][4]])