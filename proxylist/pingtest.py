import os

with open("BIG_PROXY_LIST.txt", "r") as proxy_list:
  hosts = proxy_list.readlines()
  for host in hosts:
    host = host.split(':')
    ip = host[0]
    port = host[1].split('\n')[0]
    up = True if os.system("ping -c 1 " + ip) == 0 else False
    print(ip, port, up)
    if up:
      with open("UP_PROXYS.txt", "a+") as up_list:
        up_list.write(ip+":"+port+"\n")
