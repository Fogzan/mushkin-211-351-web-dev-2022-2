# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(list_ip):
    res = []
    for elem_ip in list_ip:
        if len(elem_ip.split("-")) > 1: # Не стандартный вид
            elem_ip_split = elem_ip.split("-")[1]
            ip = elem_ip.split("-")[0]
            last_octet = int(ip.split(".")[3])
            all_octet = [ip.split(".")[0], ip.split(".")[1], ip.split(".")[2]]
            if len(elem_ip_split.split(".")) > 1: # если имеет вид 172.21.41.128-172.21.41.132
                for i in range(last_octet, int(elem_ip_split.split(".")[3]) + 1):
                    all_octet.append("{}".format(i))
                    res.append(".".join(all_octet))
                    all_octet.pop()
            elif elem_ip_split.isdigit(): # если имеет вид 1.1.1.1-3
                count_ip = int(elem_ip.split("-")[1])
                for i in range(count_ip):
                    all_octet.append("{}".format(last_octet + i))
                    res.append(".".join(all_octet))
                    all_octet.pop()
        else: # стандартный вид
            res.append(elem_ip)
    return(res)

if __name__ == "__main__":
    list_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(list_ip))