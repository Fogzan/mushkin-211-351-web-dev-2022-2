# -*- coding: utf-8 -*-

template = {
    "access_template": [
        "switchport mode access", "switchport access vlan {}",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ],

    "trunk_template": [
        "switchport trunk encapsulation dot1q", "switchport mode trunk",
        "switchport trunk allowed vlan {}"
    ]
}
quest = {
    "access" : "Введите номер VLAN: ",
    "trunk" : "Введите разрешенные VLANы: "
}

name_interface = input("Введите режим работы интерфейса (access/trunk): ")
id_interface = input("Введите тип и номер интерфейса: ")
vlans = input(quest[name_interface])

print('\n' + '-' * 30)
print("interface " + id_interface)
print("\n".join(template[name_interface + "_template"]).format(vlans))