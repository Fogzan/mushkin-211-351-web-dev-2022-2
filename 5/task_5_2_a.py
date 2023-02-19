# -*- coding: utf-8 -*-

ip_and_mask = input("Введите Ip и маску сети: ")
print('\n' + '-' * 30)
ip = ip_and_mask.split("/")[0]
mask = ip_and_mask.split("/")[1]
ip_array = ip.split(".")
bit_mask = "1" * int(mask) + "0" * (32 - int(mask))
octet_1 = int(bit_mask[0:8],2)
octet_2 = int(bit_mask[8:16],2)
octet_3 = int(bit_mask[16:24],2)
octet_4 = int(bit_mask[24:32],2)
bit_ip = "{:08b}{:08b}{:08b}{:08b}".format(int(ip_array[0]), int(ip_array[1]), int(ip_array[2]), int(ip_array[3]))
network_bit_ip = bit_ip[0:int(mask)] + "0" * (32 - int(mask))
ip_octet_1 = int(network_bit_ip[0:8], 2)
ip_octet_2 = int(network_bit_ip[8:16], 2)
ip_octet_3 = int(network_bit_ip[16:24], 2)
ip_octet_4 = int(network_bit_ip[24:32], 2)

print("Network:")
print("{:<8}  {:<8}  {:<8}  {:<8}".format(ip_octet_1, ip_octet_2, ip_octet_3, ip_octet_4))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(ip_octet_1, ip_octet_2, ip_octet_3, ip_octet_4))
print("\nMask:")
print("/" + mask)
print("{:<8}  {:<8}  {:<8}  {:<8}".format(octet_1, octet_2, octet_3, octet_4))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(octet_1, octet_2, octet_3, octet_4))