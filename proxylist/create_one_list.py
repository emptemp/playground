from pathlib import Path
result = list(Path(".").rglob("*.[tT][xX][tT]"))
#print(result)

for country in result:
  with open(country, "r") as r:
    content = r.readlines()
    print(country, content)
    if content[0] != "#\n":
      with open("BIG_PROXY_LIST.txt", "a+") as big_list:
        for ip_port in content:
          big_list.write(ip_port)

