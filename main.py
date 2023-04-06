from netmiko import ConnectHandler
import time
import csv

c = input("enter username pls : ")
b = input("enter password pls : ")
a = input("enter enable password pls : ")

with open(r'C:\Users\kamil.zeynalov\Desktop\Python\192.168_araz.csv', mode='r') as csv_file:
    csv_reader = csv_file.readlines()
print(csv_reader)

devices = {
    'device_type': 'cisco_ios',
    'ip': 'IP',
    'username': c,
    'password': b,
    'port': '2579',
    'secret': a
}
n = 1

while n < len(csv_reader):
    for line in csv_reader:

        devices['ip'] = line.strip("\n")
        print("\n\nConnecting Device ", line)

        try:
            net_connect = ConnectHandler(**devices)
            net_connect.enable()
        except:
            continue

        gateway = net_connect.send_command("sh running-config | section ip route 51.137.25.34 255.255.255.255")


        if '85.132.69.1' in gateway:
             print("Market ISP is Delta Telecom and there are no need for any changes")


        else:

         try:
            a = gateway[38:52]
            print("ISP ip address is " +a)

            net_connect.send_config_set('ip route 185.129.94.181 255.255.255.255 '+ a)


            b = net_connect.send_command("sh runn | se ip route 185.129.94.")
            print("This route added to Router   : " +b)

         except:
            continue



    n = n + 1

    time.sleep(4)
    net_connect.disconnect()
