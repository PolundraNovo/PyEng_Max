# -*- coding: utf-8 -*-
"""
Задание 9.2
Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.
У функции должны быть такие параметры:
- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (список trunk_mode_template)

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:

ключи: имена интерфейсов, вида «FastEthernet0/1»

значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    config_trunk = {}
    for param in intf_vlan_mapping.items():
        intf, vlans = param
        s_vlans = list(map(str, vlans))
        commands = []
        for command in trunk_template:
            if command.startswith("switchport trunk allowed"):
                commands.append(command + ' ' + ', '.join(s_vlans))
            else:
                commands.append(command)
        config_trunk[intf] = commands
    return config_trunk


config = generate_trunk_config(trunk_config, trunk_mode_template)
print(config)

config = generate_trunk_config(trunk_config_2, trunk_mode_template)
print(config)
