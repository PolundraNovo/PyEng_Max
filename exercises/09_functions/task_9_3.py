# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename) as f:
        for line in f:
            if line.split() and line.split()[0] == 'interface':
                intf = line.split()[-1]
            if 'vlan' in line:
                 if line.split()[1] == 'access':
                    access_dict[intf] = int(line.split()[-1])
                 else: # trunk
                    vlans = line.split()[-1].split(',')
                    vlans_int = []
                    for item in vlans:
                        vlans_int.append(int(item))
                    trunk_dict[intf] = vlans_int
    return access_dict, trunk_dict  # returns a tuple

result = get_int_vlan_map('config_sw1.txt')
print(result)
