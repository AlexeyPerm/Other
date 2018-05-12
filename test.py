import re

re_test = re.compile(r"create vlan (?P<vlan_name>\S+) tag (?P<vlan_tag>\d+)"
                     r"|config vlan \S+ \S+ untagged (?P<unt_vlan>\S+)"
                     r"|config vlan \S+ \S+ tagged (?P<tag_ports>\S+)")

with open('import.txt') as text:
    for k in re_test.finditer(text.read()):
        vlan_name = k.group('vlan_name')
        vlan_tag = k.group('vlan_tag')
        unt_vlan = k.group('unt_vlan')
        tag_ports = k.group('tag_ports')
        a = tag_ports.replace(',', ' ')
        print(vlan_name, vlan_tag, unt_vlan, a)

