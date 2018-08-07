import xlrd
from pprint import pprint

vlans_xls = 'C:\\Users\\**\\Documents\\Миграция\\upper_vlan.xlsx'
source_xls = 'C:\\Users\\**\\Documents\\Миграция\\**.xlsx'

vlans_list = xlrd.open_workbook(vlans_xls).sheet_by_index(0)
source_list = xlrd.open_workbook(source_xls).sheet_by_index(0)

with open('text.txt', 'w') as dst_file:
    for ip_address in range(1, source_list.nrows):
        # print(source_list.cell_value(ip_address, 4))
        for upper_vlan in range(1, vlans_list.nrows):
            # print('{}\t{}'.format(source_list.cell_value(ip_address, 4), vlans_list.cell_value(upper_vlan, 0)))
            if source_list.cell_value(ip_address, 4) == vlans_list.cell_value(upper_vlan, 0):
                dst_file.write(f'{source_list.cell_value(ip_address, 4)}\t\t'
                               f'{int(vlans_list.cell_value(upper_vlan, 1))}\n')
