#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.6.5+
import ipaddress

while True:
    try:
        # вводим айпишник и разбираем его на состовляющие: ip, prefix, gateway
        ip_interface = ipaddress.IPv4Interface(input('Введите IP-сети в формате 10.1.1.0/24: '))
        ip, prefix, gateway = ip_interface.ip, ip_interface._prefixlen, ip_interface.network.network_address + 1
    except ipaddress.AddressValueError:
        print('Некорректный ip. Введите заново')
    else:
        break

while True:
    try:  # Проверка корректности введёного влана
        man_vlan = int((input('Enter Management VLAN: ')))
        if 1 < man_vlan < 4096:  # проверяем корректность введёного номера влана, должен быть в диапазоне
            pass
        else:
            print('Влан должен быть в диапазоне от 2 до 4096')
            man_vlan = int((input('Введите номер VLAN ещё раз: ')))
    except ValueError:
        print('VLAN должен быть числом')
    else:
        break

intf_uplink = input('Введите uplink: ')  # Вводится имя uplink-интерфейса
systemname = ('\nsysname ' + (input('Введите sysname:  ')))
vlan_tags = []

# def interface_split(line):
#     global numbers
#     int_number = line.strip().split(' ')[5]
#     if ',' in int_number:
#         for numbers in int_number.split(','):
#     elif '-' in line:
#         for numbers in int_number.split('-'):
#     return numbers


def vlans_list(vlan_number, descr):
    result = (f"\nvlan {vlan_number}\n"
              f" description {descr}\n")
    return result


def multicast(vlan_number, descr):
    multicast_template = (f"\nvlan {vlan_number}\n"
                          f" description {descr}\n"
                          f" igmp-snooping enable\n"
                          f" multicast-vlan enable\n"
                          f"igmp-snooping enable\n")
    return multicast_template


def manage(management_vlan, ip_address, pref, gw):
    # агрументы: управляющий влан, айпишник, префикс, шлюз.
    management = (f"\n"
                  f"vlan {management_vlan}\n"
                  f" description Uprava_{management_vlan}\n"
                  f"\n"
                  f"interface Vlanif {management_vlan}\n"
                  f" ip address {ip_address} {pref}\n"
                  f"\n"
                  f"ip route-static 0.0.0.0 0.0.0.0 {gw}\n")
    return management


def uplink(uplink_intf, vlans):
    result_vlans = '\n'.join(
        [' port trunk allow-pass vlan ' + ' '.join(vlans[i:i + 10]) for i in range(0, len(vlans), 10)])
    uplink_template = ('\n'
                       f'interface {uplink_intf}\n'
                       f' description uplink\n'
                       f' port link-type trunk\n'
                       f'{result_vlans}')
    return uplink_template


def access(intf_number, vlan_number):
    access_template = (f'\ninterface Ethernet0/0/{intf_number}\n'
                       ' port link-type access\n'
                       f' port default vlan {vlan_number}\n'
                       ' loopback-detect recovery-time 300\n'
                       ' loopback-detect enable\n'
                       ' bpdu disable\n'
                       ' storm-control broadcast min-rate 500 max-rate 500\n'
                       ' storm-control multicast min-rate 500 max-rate 500\n'
                       ' storm-control action error-down\n'
                       ' storm-control enable log\n')
    return access_template


def other(other_data):
    other_conf = (f"{other_data}\n"
                  "\nclock timezone prm add 05:00:00\n"
                  "ntp-service server disable\n"
                  "ntp-service ipv6 server disable\n"
                  "ntp-service unicast-server 192.168.2.94\n"
                  "undo ip route-static 0.0.0.0 0.0.0.0 192.168.200.9\n")
    return other_conf


def trunk(trunk_intf, vlans):
    trunk_template = ('\n'
                      f'interface Ethernet0/0/{trunk_intf}\n'
                      f' port link-type trunk\n'
                      f'port trunk allow-pass vlan {vlans}\n')
    return trunk_template


with open('import.txt', 'r') as data, open('result.txt', 'a') as dst:
    for line in data:
        if line.startswith('create'):
            line_split = line.strip().split(' ')
            tag = line_split[-1]
            vlan_tags.append(tag)
            description = line_split[2]
            if not (int(tag) == 100 or int(tag) == 10):
                dst.write(vlans_list(tag, description))
            else:
                dst.write(multicast(tag, description))
        elif 'untagged' in line:
            int_number = line.strip().split(' ')[5]
            if ',' in int_number:
                for numbers in int_number.split(','):
                    dst.write(access(numbers, tag))
            elif '-' in line:
                for numbers in int_number.split('-'):
                    dst.write(access(numbers, tag))
            else:
                dst.write(access(int_number, tag))
        elif 'tagged' in line:
            int_number = line.strip().split(' ')[5]
            if ',' in int_number:
                for numbers in int_number.split(','):
                    dst.write(trunk(numbers, tag))
            elif '-' in line:
                for numbers in int_number.split('-'):
                    dst.write(trunk(numbers, tag))
            else:
                dst.write(trunk(int_number, tag))
    dst.write(uplink(intf_uplink, vlan_tags))
    dst.write(manage(man_vlan, ip, prefix, gateway))
    dst.write(other(systemname))

