# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

# Запрашиваем у пользователя ввод номера VLAN
vlan_input = int(input("Введите номер VLAN: "))

result = []

with open('CAM_table.txt') as f:
    for line in f:
        line_list = line.split()
        # Обрабатываем только строки, где первый элемент – номер VLAN (состоит только из цифр)
        if line_list and line_list[0].isdigit():
            vlan = int(line_list[0])
            # Если номер VLAN совпадает с введённым, обрабатываем строку
            if vlan == vlan_input:
                mac = line_list[1]
                interface = line_list[3]
                result.append((vlan, mac, interface))

# Сортируем результаты по VLAN (если записей несколько)
for vlan, mac, interface in sorted(result):
    print("{:<8}{:<20}{}".format(vlan, mac, interface))

