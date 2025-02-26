# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open('ospf.txt', 'r') as f:
    for line in f:
        ospf_route = line.strip().replace(',', '').split()  # Убираем запятые и разбиваем строку
        ospf_route.remove('via')  # Удаляем 'via'
        ospf_route[2] = ospf_route[2].strip("[]")  # Убираем квадратные скобки из AD/Metric

        print(template.format(ospf_route[1], ospf_route[2], ospf_route[3], ospf_route[4], ospf_route[5]))
        
